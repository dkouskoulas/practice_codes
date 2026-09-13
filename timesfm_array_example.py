import numpy as np

try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
except ImportError:
    plt = None

try:
    from timesfm import ForecastConfig, TimesFM_2p5_200M_torch
except ImportError:
    ForecastConfig = None
    TimesFM_2p5_200M_torch = None


def make_series(length: int = 100):
    """Create a simple synthetic time series with trend and seasonality."""
    t = np.arange(length)
    series = 50 + 0.8 * t + 12 * np.sin(t / 7.0)
    series += np.random.default_rng(42).normal(0, 1, size=length)
    return series.astype(float)


def plot_quantiles(values, model):
    """Plot six quantile forecasts against the true holdout data."""
    if plt is None:
        print("matplotlib is not installed; skipping plot.")
        return

    split = int(len(values) * 0.8)
    train = values[:split]
    actual = values[split:]
    horizon = len(actual)

    point_forecast, quantile_forecast = model.forecast(horizon=horizon, inputs=[train])
    q_indices = [0, 1, 2, 3, 4, 5]
    q_labels = ["Q10", "Q20", "Q30", "Q40", "Q50", "Q60"]
    x = np.arange(split, len(values))

    plt.figure(figsize=(14, 7))
    plt.plot(x, actual, label="True future", color="black", linewidth=3)
    colors = ["tab:blue", "tab:cyan", "tab:green", "tab:olive", "tab:orange", "tab:red"]
    for idx, label, color in zip(q_indices, q_labels, colors):
        q = quantile_forecast[0, :, idx]
        plt.plot(x, q, label=label, linestyle="--", linewidth=2, color=color)

    plt.title("All 6 Quantile Forecasts vs True Future Values")
    plt.xlabel("Time index")
    plt.ylabel("Value")
    plt.legend(loc="best", fontsize=10)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("timesfm_quantiles_vs_true.png", dpi=200)
    print("Saved plot to timesfm_quantiles_vs_true.png")

    plt.figure(figsize=(14, 5))
    for idx, label, color in zip(q_indices, q_labels, colors):
        q = quantile_forecast[0, :, idx]
        err = q - actual
        plt.plot(x, err, label=f"{label} error", linestyle="-", linewidth=1.8, color=color)
    plt.axhline(0, color="black", linestyle="--", linewidth=1)
    plt.title("Quantile Forecast Error Relative to True Future Values")
    plt.xlabel("Time index")
    plt.ylabel("Forecast - True")
    plt.legend(loc="best", fontsize=9)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("timesfm_quantile_errors_vs_true.png", dpi=200)
    print("Saved plot to timesfm_quantile_errors_vs_true.png")


def train_test_split_and_plot(values, model):
    """Split into 80/20 and compare actual vs predicted values."""
    if plt is None:
        print("matplotlib is not installed; skipping train/test plot.")
        return

    split = int(len(values) * 0.8)
    train = values[:split]
    test = values[split:]

    horizon = len(test)
    point_forecast, quantile_forecast = model.forecast(horizon=horizon, inputs=[train])
    pred = point_forecast[0]
    actual = test
    diff = pred - actual
    mae = np.mean(np.abs(diff))
    rmse = np.sqrt(np.mean(diff ** 2))
    mape = np.mean(np.abs(diff / np.maximum(np.abs(actual), 1e-8))) * 100

    print(f"80/20 split: train length = {len(train)}, test length = {len(test)}")
    print(f"MAE = {mae:.4f}")
    print(f"RMSE = {rmse:.4f}")
    print(f"MAPE = {mape:.2f}%")

    quantile_labels = ["Q10", "Q20", "Q30", "Q40", "Q50", "Q60"]
    quantile_mapes = []
    for i, label in enumerate(quantile_labels):
        q = quantile_forecast[0, :, i]
        q_mape = np.mean(np.abs((q - actual) / np.maximum(np.abs(actual), 1e-8))) * 100
        quantile_mapes.append((label, q_mape))
        print(f"{label} MAPE = {q_mape:.2f}%")

    print("\nTuning knobs to try for better performance:")
    print("1) Increase context length: ForecastConfig(max_context=512, max_horizon=128) -> larger values if history is longer")
    print("2) Increase horizon only when needed: choose a realistic forecast window for your use case")
    print("3) Normalize inputs when values are very large or very small: ForecastConfig(normalize_inputs=True)")
    print("4) Try different train/test splits: 70/30, 80/20, or rolling windows")
    print("5) Use a more stable series: remove trend, scale data, or detrend before forecasting")
    print("6) Use longer history if your data has seasonality or regime shifts")
    print("7) For positive data only, keep infer_is_positive=True; for mixed-sign data, consider False")
    print("8) If your series is highly noisy, smooth or aggregate it before forecasting")

    x_train = np.arange(len(train))
    x_test = np.arange(split, len(values))

    plt.figure(figsize=(12, 6))
    plt.plot(x_train, train, label="Train data", color="black", linewidth=2)
    plt.plot(x_test, actual, label="Actual test data", color="tab:blue", linewidth=2)
    plt.plot(x_test, pred, label="Predicted test data", linestyle="--", color="tab:orange", linewidth=2)
    plt.title("80/20 Train-Test Split Forecast Comparison")
    plt.xlabel("Time index")
    plt.ylabel("Value")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("timesfm_80_20_split.png", dpi=200)
    print("Saved plot to timesfm_80_20_split.png")

    plt.figure(figsize=(12, 4))
    plt.plot(x_test, diff, label="Prediction error (pred - actual)", color="tab:red", linewidth=2)
    plt.axhline(0, color="black", linestyle="--", linewidth=1)
    plt.title("Difference Between Predicted and Actual Test Values")
    plt.xlabel("Time index")
    plt.ylabel("Error")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("timesfm_80_20_error.png", dpi=200)
    print("Saved plot to timesfm_80_20_error.png")

    mape_series = np.abs((pred - actual) / np.maximum(np.abs(actual), 1e-8)) * 100
    plt.figure(figsize=(12, 4))
    plt.plot(x_test, mape_series, label="MAPE per point", color="tab:purple", linewidth=2)
    plt.axhline(np.mean(mape_series), color="black", linestyle="--", linewidth=1, label=f"Mean MAPE = {np.mean(mape_series):.2f}%")
    plt.title("MAPE by Forecast Step")
    plt.xlabel("Time index")
    plt.ylabel("MAPE (%)")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("timesfm_mape.png", dpi=200)
    print("Saved plot to timesfm_mape.png")

    plt.figure(figsize=(12, 5))
    labels = [name for name, _ in quantile_mapes]
    vals = [val for _, val in quantile_mapes]
    plt.bar(labels, vals, color=["tab:blue", "tab:cyan", "tab:green", "tab:olive", "tab:orange", "tab:red"])
    plt.axhline(np.mean(vals), color="black", linestyle="--", linewidth=1, label=f"Mean quantile MAPE = {np.mean(vals):.2f}%")
    plt.title("MAPE by Quantile")
    plt.xlabel("Quantile")
    plt.ylabel("MAPE (%)")
    plt.legend()
    plt.grid(True, axis="y", alpha=0.3)
    plt.tight_layout()
    plt.savefig("timesfm_quantile_mape.png", dpi=200)
    print("Saved plot to timesfm_quantile_mape.png")


def main():
    values = make_series(100)
    print("Input array length:", len(values))
    print("Sample values:", values[:10].tolist())

    if TimesFM_2p5_200M_torch is None or ForecastConfig is None:
        print("timesfm is not installed in this Python environment.")
        print("Use: source .venv/bin/activate && python -m pip install numpy timesfm torch")
        return

    try:
        print("Loading TimeFM model...")
        model = TimesFM_2p5_200M_torch.from_pretrained("google/timesfm-2.5-200m-pytorch")
        model.compile(ForecastConfig(max_context=512, max_horizon=128))

        point_forecast, quantile_forecast = model.forecast(horizon=12, inputs=[values])
        print("Forecast point values:")
        print(point_forecast[0][:12])
        print("Forecast quantile shape:", quantile_forecast.shape)
        plot_quantiles(values, model)

        train_test_split_and_plot(values, model)
    except Exception as exc:
        print(f"TimeFM failed to run: {exc}")
        print("If needed, run:")
        print("source .venv/bin/activate")
        print("python -m pip install numpy timesfm torch")


if __name__ == "__main__":
    main()

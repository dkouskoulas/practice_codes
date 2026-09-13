
class Probability:
    def __init__(self, p_A, p_B=None, p_A_and_B=None, p_A_or_B=None, independent=False):
        self.p_A = p_A
        self.p_B = p_B
        self.p_A_and_B = p_A_and_B
        self.p_A_or_B = p_A_or_B
        self.independent = independent

    def calc_complement_p_A(self):
        return 1 - self.p_A

    def calc_complement_p_B(self):
        return 1 - self.p_B

    def calc_intersection(self):
        if self.independent:
            if self.p_B is None:
                raise ValueError("p_B is required when events are independent.")
            return self.p_A * self.p_B

        if self.p_A_and_B is not None:
            return self.p_A_and_B

        if self.p_A_or_B is not None and self.p_B is not None:
            return self.p_A + self.p_B - self.p_A_or_B

        if self.p_B is not None:
            return self.p_A + self.p_B - self.calc_union()

        raise ValueError("Insufficient information to compute the intersection.")

    def calc_union(self):
        if self.p_A_or_B is not None:
            return self.p_A_or_B

        if self.p_B is None:
            raise ValueError("p_B is required to compute the union.")

        if self.independent:
            return self.p_A + self.p_B - (self.p_A * self.p_B)

        if self.p_A_and_B is not None:
            return self.p_A + self.p_B - self.p_A_and_B

        if self.p_B is not None:
            return self.p_A + self.p_B - self.calc_intersection()

        raise ValueError("Insufficient information to compute the union.")



class Probability:
    def __init__(self, p_A, p_B = None, p_A_and_B = None, p_A_or_B = None, independent = False):
        self.p_A = p_A
        self.p_B = p_B
        self.p_A_and_B = p_A_and_B
        self.p_A_or_B = p_A_or_B
        self.independent = independent

    def calc_complement_p_A(self):
        return 1 - self.p_A

    def calc_complement_p_B(self):
        return 1 - self.p_B

    def calc_intersection(self, p_B = None, p_A_and_B = None, p_A_or_B = None, independent = None, _use_union_fallback = False):

        if p_B is not None:
            self.p_B = p_B
        if p_A_and_B is not None:
            self.p_A_and_B = p_A_and_B
        if p_A_or_B is not None:
            self.p_A_or_B = p_A_or_B
        if independent is None:
            independent = self.independent

        if independent:
            if self.p_B is None:
                raise ValueError("p_B is required when events are independent.")
            return self.p_A * self.p_B

        if self.p_A_and_B is not None:
            return self.p_A_and_B

        if self.p_A_or_B is not None and self.p_B is not None:
            return self.p_A + self.p_B - self.p_A_or_B

        if self.p_B is not None and not _use_union_fallback:
            union_value = self.calc_union(p_B=self.p_B, independent=False, _use_intersection_fallback=True)
            return self.p_A + self.p_B - union_value

        raise ValueError("Insufficient information to compute the intersection.")

    def calc_union(self, p_B = None, p_A_and_B = None, p_A_or_B = None, independent = None, _use_intersection_fallback = False):

        if p_B is not None:
            self.p_B = p_B
        if p_A_and_B is not None:
            self.p_A_and_B = p_A_and_B
        if p_A_or_B is not None:
            self.p_A_or_B = p_A_or_B
        if independent is None:
            independent = self.independent

        if self.p_A_or_B is not None:
            return self.p_A_or_B

        if self.p_B is None:
            raise ValueError("p_B is required to compute the union.")

        if independent:
            return self.p_A + self.p_B - (self.p_A * self.p_B)

        if self.p_A_and_B is not None:
            return self.p_A + self.p_B - self.p_A_and_B

        if not _use_intersection_fallback:
            intersection_value = self.calc_intersection(p_B=self.p_B, independent=False, _use_union_fallback=True)
            return self.p_A + self.p_B - intersection_value

        raise ValueError("Insufficient information to compute the union.")


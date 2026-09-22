class MassBalance:
    
    @staticmethod
    def solids_balance(f_feed: float, f_tails: float) -> float:
        """F_feed = F_concentrate + F_tails (solids) -> F_concentrate = F_feed - F_tails"""
        return f_feed - f_tails
        
    @staticmethod
    def water_balance(water_in: float, evaporation: float = 0.0) -> float:
        """Simple water balance"""
        return water_in - evaporation
        
    @staticmethod
    def pulp_density(mass_solids: float, mass_water: float, sg_solids: float = 2.7) -> float:
        """Calculate pulp density % solids"""
        if mass_solids + mass_water == 0:
            return 0.0
        return (mass_solids / (mass_solids + mass_water)) * 100.0
        
    @staticmethod
    def circulating_load(u_solids: float, o_solids: float, f_solids: float) -> float:
        """CL = (U - O) / (O - F) where U=underflow, O=overflow, F=fresh feed"""
        if o_solids == f_solids:
            return 0.0
        return (u_solids - o_solids) / (o_solids - f_solids)

def solution(cap, n, deliveries, pickups):
    res = 0
    while deliveries and not deliveries[-1]: deliveries.pop()
    while pickups and not pickups[-1]: pickups.pop()
    
    while deliveries or pickups:
        res += max(len(deliveries), len(pickups)) * 2
        
        deliveries_cap = pickups_cap = cap
        
        while deliveries:
            if deliveries_cap >= deliveries[-1]:
                deliveries_cap -= deliveries.pop()
            else:
                deliveries[-1] -= deliveries_cap
                break
        
        while pickups:
            if pickups_cap >= pickups[-1]:
                pickups_cap -= pickups.pop()
            else:
                pickups[-1] -= pickups_cap
                break
                
    return res
        
        
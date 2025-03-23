qtd_cig = int(input("type the qtd cigarette for day: "))
years_smoking = int(input("type the years that smoking:"))

tot_day = (qtd_cig * 10)/1440
tot_years = years_smoking * 365
total = tot_day * tot_years


print(f"total of lost days: {total: 5.2f}")











def main():
	dollars = dollars_to_float(input("How much was the meal? "))
	percent = percent_to_float(input("What percentage would you like to tip? "))
	tip = dollars * percent
	print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
	# Remove the $ from dollars
    x = float(d.strip().replace('$', ''))
    return x

def percent_to_float(p):
	# Remove the % from percent
    x = float(p.strip().replace('%', '')) / 100
    return x        
main()
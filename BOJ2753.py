def is_leap_year(year):
    return (year%4==0 and year%100 != 100) or year%400 == 0

year = int(input())
ans = 1 if is_leap_year(year) else 0
print(ans)
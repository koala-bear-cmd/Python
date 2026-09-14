Month = ["January","February","March","April","May","June","July","August","September","October","November","December"]

while True:
    try:
        date = input("date:")

        if "/" in date:
            MM,DD,YYYY = date.split(sep="/")
            MM = int(MM)
            DD = int(DD)
            YYYY = int(YYYY)

            if 1 <= MM <= 12 and 1 <= DD <= 31:
                print(f"{YYYY:04}-{MM:02}-{DD:02}")
                break

        elif "/" not in date:
            MM,DD,YYYY = date.split()

            if DD.endswith(","):
                DD = DD.removesuffix(",")
                DD = int(DD)
                YYYY = int(YYYY)
                MM = Month.index(MM) + 1

                if 1 <= MM <= 12 and 1 <= DD <= 31:
                    print(f"{YYYY:04}-{MM:02}-{DD:02}")
                    break

    except ValueError:
        pass

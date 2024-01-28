import statistics as st

string = str(input())

mode = st.multimode(string)

mode.sort()
print(mode[0])
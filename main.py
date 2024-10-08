input_data = open("input.txt","r")
data = input_data.read()
data = data.split()
a = int(data[0])
b = int(data[1])
c = a + b - 1
d = c - a
r = c - b
t = str(d) + " " + str(r)
output_data = open("output.txt","w")
output_data.write(t)
input_data.close()
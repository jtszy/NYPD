import random
import os

directory_path = "/home/students/mat/j/js417940/NPD/Exercises/exercise_14_11"
directory_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

for day in directory_names:
    path = os.path.join(directory_path,day)
    os.mkdir(path)
    for time_day in ["morning","evening"]:
        path_1 = os.path.join(path,time_day)
        os.mkdir(path_1)
        path_1 = os.path.join(path_1,"Solution.csv")
        f = open(path_1,"w")
        f.write("Model; Output value; Time of computation; ")
        f.write('\n')
        res = ""
        seq_list = [["A", "B", "C"], list(range(1001)), list(range(1001))]
        for i in range(3):
            res += str(random.choice(seq_list[i]))
            if i == 2:
                res += "s"
            res += ";"
        f.write(res)
        f.close()

count = 0
for dir_1 in os.listdir(directory_path):
    path_1 = os.path.join(directory_path,dir_1)
    for dir_2 in os.listdir(path_1):
        path_2 = os.path.join(path_1,dir_2)
        f = open(os.path.join(path_2,"Solution.csv"))
        sol = f.readlines()[1]
        count += int(sol.split(";")[2][:-1])
        f.close()

print("Time of computation: ". count)


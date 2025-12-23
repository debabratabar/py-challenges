
def get_input():

    students = {}

    while True:
        name = input("Please Enter students name : ").strip()

        if name.lower() == 'done': # stop taking input 
            break 

        if name in students.keys():
            print(f"Name {name} already present ")
            continue 


        try: 
            marks = int(input(f"Please enter the Marks for Student - {name} : "))

            students[name] = marks

        except Exception as e:
            print(f" Exception - {e}")

    return students




def display_report(students):

    if not students:
        print("No students Found XXX")
        return 

    tot_students = len(students)
    avg_marks = round( sum(students.values()) / tot_students , 2 )

    max_marks = [ float('-inf') , 'none' ]
    min_marks = [float('inf') , 'none' ]
    
    for key, value in students.items():
        if value > max_marks[0] :
            max_marks[0] = value
            max_marks[1] = key

        if value < min_marks[0] :
            min_marks[0] = value
            min_marks[1] = key


    decorate = "*" * 20
    print(f"\n{decorate} \n1. Average Marks = {avg_marks}\n2. Total Students = {tot_students} \n3. Highest Marks = {max_marks[0]} - Student Name {max_marks[1]} \n4. Lowest Marks = {min_marks[0]} - Student Name {min_marks[1]}\n{decorate}")


    print("Detailed Reports ::")
    for name ,marks in students.items():
        print(f"-Marks for {name} is {marks}")


    # print(tot_students)
    # print(avg_marks)
    # print(max_marks)
    # print(min_marks)






def main():
    decorate = "*" * 20
    print(f"\n{decorate} \nStudent Marks Analyzer \n{decorate}")
    students = get_input()

    display_report(students=students)



if __name__ == '__main__':
    main()
    

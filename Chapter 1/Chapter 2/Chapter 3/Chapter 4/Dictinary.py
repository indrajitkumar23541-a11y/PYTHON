# About = {
#     "Name" : "Indrajit Kumar",
#     "Course" : "B.tech",
#     "Branch" : "Computer Science"
# }
# print(About)
# print(type(About))
Students = {
    "Name": "Indrajit Kumar",
    "Course": "B.Tech",
    "Branch": "Computer Science",
    "Marks": {
        "Python": 93,
        "C++": 87,
        "Java": 90

    }
}
#print(Students["Marks"]["Java"])
#print(len(Students.keys()))
#print(Students.values())
#print(Students.items())
#print(Students.get("Branch"))
Students.update({"C++": 80})
print(Students)

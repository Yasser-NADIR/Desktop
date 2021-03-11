import jinja2

fileSystem = jinja2.FileSystemLoader(searchpath="./templates")
env = jinja2.Environment(loader=fileSystem)
template = env.get_template("testTemplate.html")

dic = {"data1": "1", "data2": "2", "data3": "3"}
columns = ["col1", "col2", "col3"]

contents = [["a", "b", "c"], ["d", "e", "f"]]

print(template.render(columns=columns, contents=contents, len=len))
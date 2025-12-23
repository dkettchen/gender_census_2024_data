# refactor version of running file

from json import load
from vis_src.bar_charts import make_simple_bar
from vis_src.pie_charts import make_pie
from vis_utils.import_data import folders

# folder for charts 
folder = folders["charts"]
json_folder = folders["json_files"]

# load prepped data from json files
data = {}
for file in [
    "pronouns",
    "tickbox_labels",
    "pronouns_by_label",
    "location",
    "survey_source",
    "write_ins"
]:
    with open(f"{json_folder}/{file}.json", "r") as json_file:
        data[file] = load(json_file)

intersectional_bar = make_simple_bar(data["write_ins"]["Intersections"], "write_ins_intersections")
intersectional_bar.write_image(
    f"{folder}/write_in_intersections.png",
    width = 800,
    height = 600
)

male_lesbianism_pie = make_pie(
    data["write_ins"]["Conflicted queers"]["Lesbianism for men"]["#"], 
    "lesbianism_for_men"
)
male_lesbianism_pie.write_image(
    f"{folder}/lesbianism_for_men.png",
    width = 800,
    height = 800
)
female_faggotry_pie = make_pie(
    data["write_ins"]["Conflicted queers"]["Faggotry for women"]["#"], 
    "faggotry_for_women"
)
female_faggotry_pie.write_image(
    f"{folder}/faggotry_for_women.png",
    width = 800,
    height = 800
)



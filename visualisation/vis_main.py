# refactor version of running file

from json import load
from vis_src.bar_charts import make_simple_bar
from vis_utils.import_data import folders

# folder for charts 
folder = folders["charts"]

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
    with open(f"{folders["json_files"]}/{file}.json", "r") as json_file:
        data[file] = load(json_file)

intersectional_bar = make_simple_bar(data["write_ins"]["Intersections"], "write_ins_intersections")
intersectional_bar.write_image(
    f"{folder}/write_in_intersections.png",
    width = 800,
    height = 600
)
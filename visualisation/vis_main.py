# refactor version of running file

from json import load
from vis_src.bar_charts import make_simple_bar
from vis_src.pie_charts import make_pie
from vis_utils.import_data import folders
from vis_utils.colour_palettes import colours
from re import sub

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

# pronoun use by category
for categ in colours["five_categories"]:
    if " " not in categ:
        respondants = f"{categ} respondants"
    elif "direction" in categ:
        respondants = "trans respondants of unspecified direction"
    else: 
        respondants = f"respondants of {categ}"

    subbed_categ = sub("[\s\/]", "_",categ)

    pronoun_pie = make_pie(data["pronouns_by_label"][f"Pronoun sets used by {respondants}"], f"Pronoun sets used by {respondants}")
    pronoun_pie.write_image(
        f"{folder}/pronouns_by_label_pronouns_{subbed_categ}.png",
        width = 800,
        height = 800
    )
    alignment_pie = make_pie(data["pronouns_by_label"][f"Pronoun alignments of {respondants}"], f"Pronoun alignments of {respondants}")
    alignment_pie.write_image(
        f"{folder}/pronouns_by_label_pronoun_alignments_{subbed_categ}.png",
        width = 800,
        height = 800
    )

    # TODO add charts for whether trans ppl of relevant direction use trans aligned pronouns (incl balanced sets)
    if "transmasc" in categ or "transfemme" in categ:
        trans_aligned_pie = make_pie(data["pronouns_by_label"][f"Trans-aligned pronoun usage of {respondants}"], f"Trans-aligned pronoun usage of {respondants}")
        trans_aligned_pie.write_image(
            f"{folder}/pronouns_by_label_trans_aligned_usage_{subbed_categ}.png",
            width = 800,
            height = 800
        )

# intersex etc respondants
intersectional_bar = make_simple_bar(data["write_ins"]["Intersections"], "write_ins_intersections")
intersectional_bar.write_image(
    f"{folder}/write_in_intersections.png",
    width = 800,
    height = 600
)

# male lesbianism is A Transmasc Phenomenon pretty much exclusively
male_lesbianism_pie = make_pie(
    data["write_ins"]["Conflicted queers"]["Lesbianism for men"]["#"], 
    "lesbianism_for_men"
)
male_lesbianism_pie.write_image(
    f"{folder}/write_in_lesbianism_for_men.png",
    width = 800,
    height = 800
)
female_faggotry_pie = make_pie(
    data["write_ins"]["Conflicted queers"]["Faggotry for women"]["#"], 
    "faggotry_for_women"
)
female_faggotry_pie.write_image(
    f"{folder}/write_in_faggotry_for_women.png",
    width = 800,
    height = 800
)

# TODO we have one femboy whose cis status changed from cis to unspecified for some reason, 
# investigate I guess??

# TODO remake old charts so we can rerun them
# TODO rerun some charts with and without write ins 
#   -> see if any labels had a lot of additions from write-ins
sort-q2:
	python src/run_label_write_in_cleaning_code.py

clean-q2:
	python src/make_label_write_ins.py

cross-reference-q2:
	python src/cross_reference_label_write_ins.py

update-write-ins: sort-q2 clean-q2 cross-reference-q2

prep-vis-data: 
	python visualisation/vis_write_prepped_data.py

charts:
	python visualisation/vis_main.py

update-charts: prep-vis-data charts
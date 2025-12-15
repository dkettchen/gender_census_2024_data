sort-q2:
	python src/run_label_write_in_cleaning_code.py

clean-q2:
	python src/make_label_write_ins.py

cross-reference-q2:
	python src/cross_reference_label_write_ins.py

update-write-ins: sort-q2 clean-q2 cross-reference-q2
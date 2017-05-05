# File to build ECE813_report.do.txt as HTML

doconce format pandoc ECE813_report SLIDE_TYPE=remark SLIDE_THEME=light
doconce slides_markdown ECE813_report remark --slide_theme=light


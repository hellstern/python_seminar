# Water chart - demo
# pyecharts

# HTML- Plot
c = (
 Liquid()
 .add("Solgt", [0.6])
 .set_global_opts(title_opts=opts.TitleOpts(title="% af salget opnået", pos_left="center"))
 .render("water.html")
)




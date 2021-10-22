
def generate_table(header, ):
    # okay, this is probably a stupid way to do this.
    # the jinja templating engine is there for a reason!
    output_string = ""

    table_string = '<table class="table table-striped table-hover table-dark" id="projects_table">'

    output_string += "<thead><tr>
	for i in header:
	    <th style=""> i</th>
							<th style="">ID</th>
							<th style="">Blurb</th>
						</tr>
					</thead>

				<tbody>
				</tbody>
			</table> -->
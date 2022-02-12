% include('header.tpl')

<div>, tags=tags</div>

<div id="content" class="mui-container-fluid">

	<div class="mui-row">
		<div class="mui-col-sm-10 mui-col-sm-offset-1">
			<div class="mui--text-dark-secondary mui--text-body2">
				<h1>
					RESOURCES ({{ len(resources) }})
					% if search_tag:
						<small>&nbsp;(<a href="/">show all</a>)</small>
					% end
				</h1>
			</div>
			<div class="mui-divider"></div>
			<table>
				<thead>
					<tr>
						<th>#</th>
						<th>Name</th>
						<th>Type</th>
						<th>Priority</th>
					</tr>
				</thead>
				% for resource in resources:
				<tbody>
					<tr>
						<td>{{ resource['id'] }}</td>
						<td>{{ resource['name'] }}</td>
						<td>{{ resource['type'] }}</td>
						<td>{{ resource['priority'] }}</td>
					</tr>
				</tbody>
				% end
			</table>
		</div>
	</div>

</div>

% include('footer.tpl')

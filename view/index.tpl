% include('header.tpl')

<div id="content" class="mui-container-fluid">
	<div class="mui-row">
		<div class="mui-col-sm-10">

			<div class="mui--text-dark-secondary mui--text-body2">
				<h1>
					Resource allocation system ({{ len(resources) }})
				</h1>
			</div>
			<div class="mui-divider"></div>
			<button class="mui-btn mui-btn--primary" onclick="go_new()">NEW RESOURCE</button>
			% if len(resources) > 0:
			<table class="mui-table">
				<thead>
					<tr>
						<th>#</th>
						<th>Name</th>
						<th>Type</th>
						<th>Priority</th>
						<th>Status</th>
						<th>Actions</th>
					</tr>
				</thead>
				% for resource in resources:
				<tbody>
					% if resource.is_occupied == 0:
					<tr class="row-available">
						<td>{{ resource.id }}</td>
						<td>{{ resource.name }}</td>
						<td>{{ resource.type }}</td>
						<td>{{ resource.priority }}</td>
						<td>AVAILABLE</td>
						<td><button class="mui-btn mui-btn--primary" title="Register to available resource" onclick="do_register({{ resource.id }})">REGISTER</button></td>
					</tr>
					% end
					% if resource.is_occupied == 1:
					<tr class="row-occupied">
						<td>{{ resource.id }}</td>
						<td>{{ resource.name }}</td>
						<td>{{ resource.type }}</td>
						<td>{{ resource.priority }}</td>
						<td>OCCUPIED</td>
						<td><button class="mui-btn mui-btn--danger" title="Release occupied resource" onclick="do_release({{ resource.id }})">RELEASE</button></td>
					</tr>
					% end
				</tbody>
				% end
			</table>
			% end
		</div>
	</div>

</div>


<script>
	function go_new() {
		location.href = '/new'
	}

	async function do_register(id) {
		await fetch(`/register/${id}`)
                .then(data => {
                location.href = '/'
                })
	}

	async function do_release(id) {
		await fetch(`/release/${id}`)
                .then(data => {
                location.href = '/'
                })
	}
</script>

% include('footer.tpl')

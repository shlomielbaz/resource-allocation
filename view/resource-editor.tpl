% include('header.tpl')

<div id="content" class="mui-container-fluid">
    <div class="mui-row">

        <div class="mui-col-sm-10">
            <div class="mui--text-dark-secondary mui--text-body2">
                <h1>
                    Add New Resource
                </h1>
            </div>
            <div class="mui-divider"></div>

            <form class="mui-form" id="resource-form" onsubmit="save_resource(event);" method="POST">
                <div class="mui-textfield">
                    <input type="text" name="name" placeholder="Resource Name" required />
                </div>
                <div class="mui-textfield">
                    <input type="text" name="type" placeholder="Resource Type (server/desktop)" required />
                </div>

                 <div class="mui-textfield">
                    <input type="number" name="priority" placeholder="Resource Priority 1..5" min="1" max="5" />
                </div>

                <button type="submit" class="mui-btn mui-btn--primary">SAVE RESOURCE</button>
                <button type="submit" class="mui-btn mui-btn--raised" onclick="cancel()">CANCEL</button>
            </form>
        </div>
    </div>
</div>

<script>
    async function save_resource(event) {
        event.preventDefault();

        const type = document.forms['resource-form']['type'].value;

        if (type != 'server' && type != 'desktop') {
            alert("Resource type should be 'server' or 'desktop'");
            return false
        }
        const data = {
            name: document.forms['resource-form']['name'].value,
            type: type,
            priority: 1
        };
        const response = await fetch('/new', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });

        location.href = '/'
    }

    function cancel() {
        location.href = '/'
    }
</script>

% include('footer.tpl')

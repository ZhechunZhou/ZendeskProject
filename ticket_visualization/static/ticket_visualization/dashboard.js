function getTickets() {
    $.ajax({
        url: "get_tickets",
        dataType: "json",
        success: updatePage,
        error: updateError
    });
}

function updatePage(response) {
    if (Array.isArray(response)) {
        updateChart(response)
        updateList(response)
    } else if (response.hasOwnProperty('error')) {
        displayError(response.error)
    } else {
        displayError(response)
    }
}

function updateError(xhr, status, error) {
    displayError('Status=' + xhr.status + ' (' + error + ')')
}

function displayError(message) {
    $("#error").html(message);
}

function updateList(items) {
    if (items.length === 0) {
        console.log("the list is empty");
        return;
    }

    let table = document.getElementById("ticket_table");
    //check if the ticket table is created
    if (!$("#ticket_table_header").length) {
        //get header as name of attributes in a ticket
        var header = [];
        for (let key in items[0]) {
            if (header.indexOf(key) === -1) {
                header.push(key);
            }
        }

        //add header to table
        let headerRow = table.insertRow(-1);
        headerRow.id = "ticket_table_header";
        for (let i = 0; i < header.length; i++) {
            let th = document.createElement("th");
            th.id = "attribute_" + i;
            th.innerHTML = header[i];
            headerRow.appendChild(th);
        }
    }

    // Adds each new todolist item to the list (only if it's not already here)
    $(items).each(function () {
        let my_id = "id_ticket_" + this.id
        if (document.getElementById(my_id) == null) {
            let row = table.insertRow(-1);
            row.id = my_id;
            for (let key in this) {
                let cell = row.insertCell(-1);
                cell.innerHTML = this[key];
            }
        }
    })
}

function updateChart(items) {
    let dateTickets = {}
    $(items).each(function () {
        if (!dateTickets.hasOwnProperty(this["created_at"])) {
            dateTickets[this["created_at"]] = 1;
        } else {
            dateTickets[this["created_at"]] = dateTickets[this["created_at"]] + 1;
        }
    });
    console.log(Object.keys(dateTickets));
    console.log(Object.values(dateTickets));
    let chartDom = document.getElementById("ticket_chart");
    let myChart = echarts.init(chartDom);
    let option;

    option = {
        xAxis: {
            type: 'category',
            boundaryGap: false,
            data: Object.keys(dateTickets)
        },
        yAxis: {
            type: 'value'
        },
        series: [{
            data: Object.values(dateTickets),
            type: 'line',
            areaStyle: {}
        }]
    };

    if (option && typeof option === 'object') {
        myChart.setOption(option);
    }

}

function sanitize(s) {
    // replace ampersand
    return s.replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/"/g, '&quot;')
}
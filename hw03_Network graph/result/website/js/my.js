$.getJSON("../../data/graph_data.json", function (json) {
    // console.log(json); // this will show the info it in firebug console

    // console.log(json['nodes'].length)
    $('#nodes-number').html(json['nodes'].length);
    // console.log(json['links'].length)
    $('#edges-number').html(json['links'].length);

    nodeTable(json['nodes'])
    edgeTable(json['links'])

    function nodeTable(list) {
        var top = Math.min(list.length, 30);
        for (var i = 0; i < top; i++) {
            // append each column to the row
            var row = $('<tr/>');
            row.append($('<td/>').html(i + 1));
            row.append($('<td/>').html(list[i]['id']));
            row.append($('<td/>').html(list[i]['value']));

            // console.log(i)
            // console.log(list[i]['id'])
            // console.log(list[i]['value'])

            // append each row to the table
            $("#nodes-table").append(row);
        }
    }

    function edgeTable(list) {
        var top = Math.min(list.length, 30);
        for (var i = 0; i < top; i++) {
            // append each column to the row
            var row = $('<tr/>');
            row.append($('<td/>').html(i + 1));
            row.append($('<td/>').html(list[i]['source']));
            row.append($('<td/>').html(list[i]['target']));
            row.append($('<td/>').html(list[i]['value']));

            // append each row to the table
            $("#edges-table").append(row);
        }
    }
});
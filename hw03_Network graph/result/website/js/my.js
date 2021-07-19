$(function () {
    // load 2D and 3D network graph
    $("#frame1").load("3D_network.html")
    $("#frame2").load("2D_network.html")

    // initial only show 3D network
    $("#frame1").show()
    $("#frame2").hide()

    // show 3D network
    $("#b1").click(function () {
        $("#frame1").show()
        $("#frame2").hide()
        $("#b1").attr('class', 'btn btn-primary');
        $("#b2").attr('class', 'btn btn-outline-primary');
    })

    // show 2D network
    $("#b2").click(function () {
        $("#frame1").hide()
        $("#frame2").show()
        $("#b1").attr('class', 'btn btn-outline-primary');
        $("#b2").attr('class', 'btn btn-primary');
    })
});

var node_json;
var edge_json;

$.getJSON("../../data/graph_data.json", function (json) {
    // console.log(json); // this will show the info it in firebug console

    node_json = json['nodes'];
    edge_json = json['links']
    var node_num = node_json.length;
    var edge_num = edge_json.length;

    // console.log(json['nodes'].length)
    $('#nodes-number').html(node_num);
    $('#node-upper').html(node_num);
    // console.log(json['links'].length)
    $('#edges-number').html(edge_num);
    $('#edge-upper').html(edge_num);

    // create slider of nodes and edges
    createNodeSlider(node_num);
    createEdgeSlider(edge_num);

    // initial table of nodes and edges
    nodeTable(Math.min(10, node_num))
    edgeTable(Math.min(10, edge_num))
});

function nodeTable(top) {

    // clear table
    $("#nodes-table").empty();

    $('#node-top').html(top);
    for (var i = 0; i < top; i++) {
        // append each column to the row
        var row = $('<tr/>');
        row.append($('<td/>').html(i + 1));
        row.append($('<td/>').html(node_json[i]['id']));
        row.append($('<td/>').html(node_json[i]['value']));

        // append each row to the table
        $("#nodes-table").append(row);
    }
}

function edgeTable(top) {

    // clear table
    $("#edges-table").empty();

    $('#edge-top').html(top);
    for (var i = 0; i < top; i++) {
        // append each column to the row
        var row = $('<tr/>');
        row.append($('<td/>').html(i + 1));
        row.append($('<td/>').html(edge_json[i]['source']));
        row.append($('<td/>').html(edge_json[i]['target']));
        row.append($('<td/>').html(edge_json[i]['value']));

        // append each row to the table
        $("#edges-table").append(row);
    }
}

function createNodeSlider(len) {
    $("#nodes-slider").slider({
        min: 1,
        max: len,
        value: Math.min(10, len),
        create: function (e, ui) {
            var style = { "width": "40px", "text-align": "center" };
            $(this).find(".ui-slider-handle").css(style);
            $(this).find(".ui-slider-handle").html(Math.min(10, len));
        },
        slide: function (e, ui) {
            // $("#").html(ui.value);
            $(this).find(".ui-slider-handle").html(ui.value);
        },
        change: function (e, ui) {  // when change value
            // console.log(ui.value);
            nodeTable(ui.value);    // re-render table
        }
    });
}

function createEdgeSlider(len) {
    $("#edges-slider").slider({
        min: 1,
        max: len,
        value: Math.min(10, len),
        create: function (e, ui) {
            var style = { "width": "40px", "text-align": "center" };
            $(this).find(".ui-slider-handle").css(style);
            $(this).find(".ui-slider-handle").html(Math.min(10, len));
        },
        slide: function (e, ui) {
            // $("#").html(ui.value);
            $(this).find(".ui-slider-handle").html(ui.value);
        },
        change: function (e, ui) {  // when change value
            // console.log(ui.value);
            edgeTable(ui.value);    // re-render table
        }
    });
}
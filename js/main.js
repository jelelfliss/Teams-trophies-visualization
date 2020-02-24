/*/0. Calling the python script

window.onload = function () {
    $.ajax({
        mimeType: 'text/plain; charset=x-user-defined',
        type: 'POST',
        datatype: "text",
        url: "data/update.py",
        success: function () {
            alert("WORKING !")
        },
        error: function () {
            alert("Not Working ... ")
        }
    });
};

*/
//1. Variables
var color_flag;
var previous_flag;

var interval;
var new_data;

var legend_is_written = false;

var Teams = [];
var Countries = [];
var first_season
var season_count = 0
var margin = {
    top: 100,
    bottom: 100,
    left: 100,
    right: 180
}
var svg_height = 500;
var svg_width = document.getElementById("chart-area").offsetWidth / 1.25;

var height = svg_height - margin.top - margin.bottom;
var width = svg_width - margin.right - margin.left;

var Teams_Colors = {
    "Real Madrid": "#fced67",
    "FC Barcelona": "#1b00ff",
    "Juventus": "#7a7a7a",
    "Liverpool": "#cf0000",
    "Manchester United": "#ff3007",
    "Borussia Dortmund": "#00137c",
    "Manchester City": "#42c0ff",
    "Chelsea FC": "#e2d400",
    "Bayern Munich": "#e31b1b",
};



//2. Adding the SVG canvas
var g = d3.select("#chart-area").append("svg")
    .attr("height", svg_height)
    .attr("width", svg_width)
    .append("g") // 2.1 Adding the vizualization sector group
    .attr("class", "sector")
    .attr("transform", "translate(" + margin.left + "," + margin.bottom + ")")

//3. Adding the scales 
// 3.1 Adding the X Scale : the League_trophies axis
var x_scaling = d3.scaleLinear()
    .range([0, width])
    .domain([-2, 30]);

// 3.2 Adding the Y Scale : The Cup_trophies axis
var y_scaling = d3.scaleLinear()
    .range([height, 1])
    .domain([-2, 30]);

// 3.3 Adding the circle shape scale : UEFA 
var area_scaling = d3.scaleLinear()
    .range([5, 35])
    .domain([0, 15])

// 3.4 Color Scales 
var color_scaling;

var country_color_scaling = d3.scaleOrdinal(d3.schemeAccent);

//4. Axis Calls 
// 4.1 Initialize the axis's
var x_axis_call = d3.axisBottom(x_scaling)
    .tickFormat(function (d) {
        return +d;
    })
var y_axis_call = d3.axisLeft(y_scaling)
    .tickFormat(function (d) {
        return +d;
    })

// 4.2 Calling the axis's
g.append("g")
    .attr("class", "x_axis")
    .attr("transform", "translate(0," + height + ")")
    .call(x_axis_call);
g.append("g")
    .attr("class", "y_axis")
    .call(y_axis_call);


//5. X & Y & Seasons Labels

g.append("text")
    .attr("class", "X_Label")
    .attr("y", height + 50)
    .attr("x", width / 2)
    .attr("font-size", "20px")
    .attr("text-anchor", "middle")
    .text("League wons")
    .attr("opacity", "0.5")

g.append("text")
    .attr("class", "Y_Label")
    .attr("y", -50)
    .attr("x", -150)
    .attr("font-size", "20px")
    .attr("text-anchor", "middle")
    .text("Local Cup wons")
    .attr("transform", "rotate(-90)")
    .attr("opacity", "0.5")

var Season_label = g.append("text")
    .attr("class", "Season")
    .attr("y", height - 20)
    .attr("x", width - 100)
    .attr("font-size", "35px")
    .attr("text-anchor", "middle")
    .text("Season here")
    .attr("opacity", "0.4");

//6. Getting the flag color Function
function getting_flag_color() {
    return $("input[name='flag_for_coloring']:checked").val();
}

//7. Tooltip
var tip = d3.tip().attr("class", "d3-tip").html(function (d) {
    var output = "<strong>Team :</strong> <span style='color:#ffb17f;'>" + d.Team + "</span><br>";
    output += "<strong>Local Cups Wons :</strong> <span style='color:#ffb17f;'>" + d.CUP + "</span><br>";
    output += "<strong>League Wons :</strong> <span style='color:#ffb17f;'>" + d.League + "</span><br>";
    output += "<strong>UEFA Champions League Wons :</strong> <span style='color:#ffb17f;'>" + d.UEFA_CUP + "</span>";
    return output;
});

g.call(tip);

//8. Legend 
var legend = g.append("g")
    .attr("transform", "translate(" + (width + 165) + "," + (height - 250) + ")")
    .attr("class", "Legend_Holder");

function Legend_Writing(List, Scale_Type) {
    List.forEach(function (element, i) {
        var legendrow = legend.append("g")
            .attr("class", "Legend_Elements")
            .attr("transform", "translate(0," + (i * 20) + ")")
        legendrow.append("rect")
            .attr("width", 10)
            .attr("height", 10)
            .attr("fill", Scale_Type(element));

        legendrow.append("text")
            .attr("class", "Legend_Elements")
            .attr("x", -10)
            .attr("y", 10)
            .attr("text-anchor", "end")
            .style("text-transform", "capitalize")
            .text(element);
    })
    legend_is_written = true;
}






d3.json("data/data.json").then(function (data) {

    // Getting the first season and store it in a variable 
    first_season = +data[0].season;
    // Format Data By converting the trophie numbers from strings to int's 
    new_data = data.map(function (team) {
        return team.teams;
    })

    

    // Process of getting the teams list & Countries list

    new_data[0].forEach(function (d) {
        Teams.push(d.Team);
        if (Countries.indexOf(d.Country) == -1) {
            Countries.push(d.Country);
        }
    })

    // Getting the colors list 
    var teams_colors_list = [];
    for (Key in Teams_Colors) {
        if (Teams.indexOf(Key) != -1) {
            teams_colors_list.push(Teams_Colors[Key]);
        }
    }
    console.log(Teams);
    console.log(teams_colors_list);

    color_scaling = d3.scaleOrdinal().range(teams_colors_list)
        .domain(Teams);

    // Loop

    d3.interval(function () {

    }, 75);

    // First run of the visualization
    update(new_data[0]);


});

function step() {
    // At the end of our data, loop back
    season_count = (first_season + season_count < 2020) ? season_count + 1 : 0
    update(new_data[season_count]);

}

$("#play-btn")
    .on("click", function () {
        var button = $(this);
        if (button.text() == "Play") {
            button.text("Pause");
            interval = setInterval(step, 100);
        } else {
            button.text("Play");
            clearInterval(interval);
        }
    });

$("#reset-btn")
    .on("click", function () {
        season_count = 0;
        update(new_data[0]);
    });

$("#season-slider").slider({
    max: 2019,
    min: 1956,
    step: 1,
    slide: function (event, ui) {
        season_count = ui.value - 1956;
        update(new_data[season_count]);
    }
});



$("#flag_team").on("change",function(){
    update(new_data[season_count]);
})
$("#flag_country").on("change",function(){
    update(new_data[season_count]);
})

function update(data) {

    $( "#season-slider" ).slider( "option", "value", season_count+1956 );

    // Updating the legend According to the radio selecion

    previous_flag = color_flag;
    color_flag = getting_flag_color();
    if (previous_flag != color_flag) {
        // If flag has changed then legend must change too
        legend_is_written = false;
        if (color_flag == 0) {
            d3.selectAll(".Legend_Elements").remove()
            Legend_Writing(Teams, color_scaling);

        } else {
            d3.selectAll(".Legend_Elements").remove()
            Legend_Writing(Countries, country_color_scaling);
        }
    }



    var t = d3.transition().duration(100);
    // JOIN new data with old elements
    var circles = g.selectAll("circle").data(data, function (d) {
        return d.Team
    });

    // EXIT old elements not present in new data
    circles.exit().attr("class", "exit").remove();

    // ENTER new elements present in new data
    circles.enter()
        .append("circle")
        .attr("class", "enter")
        .on("mouseover", tip.show)
        .on("mouseout", tip.hide)
        .merge(circles)
        .transition(t)
        // UPDATE new elements in old data
        .attr("fill", function (d) {
            if (color_flag == 1) {
                return country_color_scaling(d.Country);
            } else {
                return color_scaling(d.Team);
            }

        })
        .attr("cx", function (d) {
            return x_scaling(d.League);
        })
        .attr("cy", function (d) {
            return y_scaling(d.CUP);
        })
        .attr("r", function (d) {
            return area_scaling(d.UEFA_CUP);
        })
        //.attr("stroke", "black");
    // Updating the season label 
    var current_season_year2 = season_count + first_season;
    var current_season_year1 = current_season_year2 - 1
    Season_label.text(current_season_year1 + "-" + current_season_year2);
    // Updating the slider label
    $("#year1")[0].innerHTML = +(1955+season_count);
    $("#year2")[0].innerHTML = +(1956+season_count);
}

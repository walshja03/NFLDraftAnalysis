
//pull in data from outputfile.js which corresponds to my chosen model
tableData = resultsdata
//save the size for use in the filters js
var size = tableData.length

//Populate table with data from my model on initial load
tableData.forEach(function (ufoReport) {
    // console.log(ufoReport)
    var row = d3.select("tbody").append("tr");
    Object.values(ufoReport).forEach(v => {
        // console.log(v);
        row.append("td").text(v);
    })
})

//List of attributes that a model can be run by
var optdata = ['ExcludeZeroFPTS','pickNum','Conf','Class','Age', 'Wt', 'Forty', 'Vertical', 'BenchReps', 'BroadJump', 'ThreeCone', 'Shuttle',
'careerRec', 'careerRecYds', 'careerYPC', 'careerRecTds',
'careerRushAtt', 'careerRushYds', 'careerYPA', 'careerRushTds',
'careerPlays', 'careerTotalYds', 'careerYPT', 'careerTotalTds',
'dr_1games', 'dr_1Rec', 'dr_1RecYds',
'dr_1YPC', 'dr_1RecTds', 'dr_1RushAtt', 'dr_1RushYds', 'dr_1YPA',
'dr_1RushTds', 'dr_1Plays', 'dr_1TotalYds', 'dr_1YPT', 'dr_1TotalTds',
'dr_2games', 'dr_2Rec', 'dr_2RecYds', 'dr_2YPC', 'dr_2RecTds',
'dr_2RushAtt', 'dr_2RushYds', 'dr_2YPA', 'dr_2RushTds', 'dr_2Plays',
'dr_2TotalYds', 'dr_2YPT', 'dr_2TotalTds', 'dr_3games', 'dr_3Rec',
'dr_3RecYds', 'dr_3YPC', 'dr_3RecTds', 'dr_3RushAtt', 'dr_3RushYds',
'dr_3YPA', 'dr_3RushTds', 'dr_3Plays', 'dr_3TotalYds', 'dr_3YPT',
'dr_3TotalTds']

//append a list of option to the create a model page on initial load
var list = d3.select(".panel-body").append("dl");
list.selectAll("input")
    .data(optdata)
    .enter()
    .append('dt')
        .attr('value', function (d, i) { return d; })
        .text(function (d) { return `${d}  `; })
    .append("input")
        .property("checked", false)
        .attr("type", "checkbox")
        .attr("id", function (d, i) { return d; })




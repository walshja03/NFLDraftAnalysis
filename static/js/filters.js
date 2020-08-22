// Select the button
var button = d3.select("#filter-btn");


// Create event handler for run model button that will kick off find info
button.on("click", findinfo);



//function to append select items from the page to a list to be sent to model
function addSelects() {
    var selectedIds = [];
    var ids = optdata
    

    for ( var i = 0; i < ids.length; i++) {
        var checked = d3.select(`#${ids[i]}`).property("checked")
        if (checked) {
            console.log(ids[i])
            selectedIds.push(ids[i]);
        }
    }
    console.log(selectedIds)
    return selectedIds
}

//function that will take in the inputs, send to the model, recieve the result and display on the page
function findinfo() {

    //prevent page reload
    d3.event.preventDefault();

    //clear the current table elements
    var chosen = addSelects();
    body = d3.select("tbody")
    body.html("")

    //send the chosen stats a string to go to python for running the model
    fetch("/model",
        {
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            method: "POST",
            body: JSON.stringify(chosen)
        })

        //promise that if the response comes back then append a table
        .then(function (res) {
            return res.json()
            console.log("here")
        }).then(function (data) {

            //clear existing table
            body = d3.select("tbody")
            body.html("")
            console.log(size)
            var i;
            // console.log(data["Player_x"].length)
            for (i=0;i<size;i++){
                var row = d3.select("tbody").append("tr");
                row.append("td").text(data["Rank"][i]);
                row.append("td").text(data["Player_x"][i]);
                row.append("td").text(data["projected points"][i]);
                // console.log(i)

            } 

        })
        .catch(function (res) { console.log(res.body) })
}











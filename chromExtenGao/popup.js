console.log("This is a popup!")

// console.log("This is a popup!) 


// window.alert("it begains!")


var URLofService = "http://116.205.178.204:3002/timRecieve?timMethod=retrieveOneContent&content=thisIsUseLessContentForRetrevingAll"

// postRespon = requests.post( URLofService +  "/timRecieve", data={'timMethod':'inputContent','content':theItemToAdd})

// var timURL = URLofService + ""


var xhr = new XMLHttpRequest()

xhr.open('GET',URLofService)

xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded')

// xhr.send("'timMethod'='inputContent'&'content'=theItemToAdd'")  

xhr.send()



xhr.onreadystatechange = function () {
    if(xhr.readyState === 4 && xhr.status === 200) {
        
        console.log("it has done")

        console.log(xhr.response)

        console.log("SIX")

        console.log(xhr.responseText[1]);

        console.log("SIX")

        var b = xhr.responseText.slice(1)

        b = b.slice(0, b.length - 1)

        

        console.log( b );

        // rpText = xhr.responseText;

        // print(rpText)

        // console.log(typeof(xhr.responseText))

        var xhrJson = JSON.parse(b) 
        
        console.log("content of xhrJson is >> " ,  xhrJson)

        console.log("SIX")

        console.log(xhrJson["data"]["content"])

        var contentIWant = xhrJson["data"]["content"]

        console.log("SIX")

        console.log(contentIWant)

        // console.log(typeof(xhrJson))

        // console.log(xhrJson["_id"])

        var six = document.getElementById("neoContent")

        var textnode = document.createTextNode(contentIWant)

        six.appendChild(textnode);

        // document.getElementById("neoContent").appendChild(six);

    }
    else{
        console.log("state changing!")
        // console.log(xhr.responseText);
    }
}


// xhr.responseText

console.log("six")

console.log(xhr.responseText)

// console.log(typeof(xhr.responseText))

// var xhrJson = JSON.parse(xhr.responseText)   

// console.log(typeof(xhrJson))









// AA
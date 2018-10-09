    
    if (nameArray1.length >= nameArray2.length) {
        var longArray = nameArray1;
        var shortArray = nameArray2;
    } else {
        var longArray = nameArray2;
        var shortArray = nameArray1;
    }
    
    var longLen = longArray.length;
    var shortLen = shortArray.length;
    var numberStudents = longLen + shortLen;
    var bothGroups = longArray.concat(shortArray);
    
    var longAttend = []; 
    var shortAttend = [];
    var attend = [];
    for(var n = 0; n < longLen; n++) {
        longAttend[n] = longArray[n].fields.attend;
    };
    for(var n = 0; n < shortLen; n++) {
        shortAttend[n] = shortArray[n].fields.attend;
    };
    for(var n = 0; n < numberStudents; n++) {
        attend[n] = bothGroups[n].fields.attend;
    };
           
    console.log(nameArray1);
        
    var previousGroups = 0;  // # groups of previous freeze
    var moving = false;
    
    var interval;  // for the interval function that scrambles the names

    var groupMade = false;
    

    var studentCol1 = document.getElementById('student-column1');
    var studentCol2 = document.getElementById('student-column2');
    var studentPairs = document.getElementById('student-pairs');
    var vertGap = 30;
    var divChoice = document.createElement('div');                
    divChoice.id = "choicename";

    divChoice.innerHTML = " ";
    studentPairs.appendChild(divChoice);

    var setNames = function(nArray,) {
        var h = 0;
        for(var n = 0; n < nArray.length; n++){   //place the names on the screen
            var divName = "floatName" + n;
            var names = nArray[n].fields.nickname;
            var divTag = document.createElement('div');
            divTag.id = divName;
            divTag.innerHTML = names;
            divTag.style.position = "absolute";
            if (attend[n] == true) {
                divTag.style.textDecoration = "none";
            } else {
                divTag.style.textDecoration = "line-through";
                divTag.style.color = 'red';
            };
          
            h = n - Math.floor(n/longLen)*longLen;  // go back up to the top of the name column
            
            divTag.style.top = (10 + h * vertGap) + "px";
            //divTag.style.left  = horz + "px";
            divTag.style.fontSize = "14px";
            divTag.className = "randomFloat";
            divTag.onclick = boldText;
             
            if (Math.floor(n/longLen)+1 == 2) {
                studentCol2.appendChild(divTag);
            } else {
                studentCol1.appendChild(divTag);
            }; 
        };
    };

    setNames(bothGroups);
        
    $( "#go" ).click(function() {
        moving = true;
        //clear the previous random name choice if there is one
        var divfc = document.getElementById('choicename');
        while(divfc.firstChild) {            
            divfc.removeChild(divfc.firstChild);
        };
        
        //clear the group titles
        if (groupMade == true) {
            clearGroups();
        }
        
        // move the floatNames divs around aka "the scrambler"
        var gotime = 1;
        interval = setInterval(function () {
            for(var i = 0; i < (numberStudents + 1); i++){
                var divName = "floatName" + i;
                if (attend[i] == true) {
                    $( "#" + divName ).css({
                        left: (Math.random()*500+300) + "px",
                        top: (Math.random()*350 + 40) + "px",
                        "font-size": "20px",
                    });
                };
            };
            gotime += 1;
            if (gotime > 100) {
                clearInterval(interval);
               }
        }, 500);
    });

    /* $( "#stop" ).click(function() {
        if (moving == true) {
            clearInterval(interval);
            choosePerson(0, numberStudents);
            setTimeout(clearDivs, 1000);
        };
        moving = false;
    }); */
    
    var clearDivs = function() {
        for(var i = 0; i < (numberStudents); i++) {
            divn = "floatName" + i;
            var elem = document.getElementById(divn);
            elem.remove();
            };
        setNames();
        };
        
    var clearGroups = function() {
        console.log(previousGroups);
        for (i = 0; i < previousGroups; i++) {  //remove the previous # of groups
            num = (i+1);
            var divn = "Group" + num.toString();
            var elem = document.getElementById(divn);
            elem.remove();
            };
        clearDivs();
        groupMade = false;
        }; 
        
                                 
    function boldText(){
        var togname = this.id.split('floatName').join('');  // get the id # from the element
        console.log(togname);
        if (this.style.textDecoration == 'none') {
            this.style.textDecoration = 'line-through';
            this.style.color = 'red';
            attend[togname] = false;
        } else {
            this.style.textDecoration = 'none';
            this.style.color = 'black';
            attend[togname] = true;
        }
    };
        
    // knuff-shuffle to mix the list of students
    function shuffle() {
        var array = [];
        for (var n=0; n<numberStudents; n++) {
            array[n-0] = n;
        }
        var currentIndex = array.length
          , temporaryValue
          , randomIndex
          ;

        // While there remain elements to shuffle...
        while (0 !== currentIndex) {

          // Pick a remaining element...
          randomIndex = Math.floor(Math.random() * currentIndex);
          currentIndex -= 1;

          // And swap it with the current element.
          temporaryValue = array[currentIndex];
          array[currentIndex] = array[randomIndex];
          array[randomIndex] = temporaryValue;
        }

        return array;
    }
    
    function grouping() {
        var ns = 0;
        var nl = 0;
        var nTotal = 0;
        // make sure to not count students that are away
        for (n=0; n < longLen; n++) {
            if (attend[n] == true) {
                nl++
            };
        };
        for (n=longLen; n < shortLen; n++) {
            if (attend[n] == true) {
                ns++
            };
        };

        var totalGroups = Math.max(nl,ns);
        
        return [totalGroups, nTotal]; 
    }
    
    function sort() {
        var i = 0;
        var sortName  = [];
        var groupNumbers = [];
        var placeCount = 0;
        var groupDown = 0;
        var groupLeft = 0;
        groupMade = true;
        var studentAttend = 0;
        var leftOver = 0;
        
        // get the random order of students
        var groups = grouping();
        previousGroups = groups[0];
        
        // shuffle the order of the students
        var longOrder = shuffle(longArray);
        var shortOrder = shuffle(shortArray);
        
        // place the group headings
        for (i = 0; i < groups[0]; i++) {
            num = (i+1);
            divGroup = document.createElement('div');
            divGroup.innerHTML = "Group " + num.toString();
            divGroup.id = "Group" + num.toString();
            num = num*120-120;
            divGroup.style.width = "110px";
            divGroup.style.fontSize = "20px";
            divGroup.style.fontWeight = "bold";
            divGroup.style.color = "blue";
            divGroup.style.position = "absolute";
            divGroup.style.top = "100px";
            divGroup.style.left = num.toString() + "px";
            studentCol1.appendChild(divGroup);
        }
        
        // fill each row
        for (i = 0; i < numberStudents; i++) {
            var divName = "floatName" + studentOrder[i];
            var SO = studentOrder[i];
            console.log(document.getElementById(divName).parentNode);
            
            if (attend[SO] == true) {
                var stdId = document.getElementById(divName);
                stdId.parentNode.id = "studentCol1";
                studentCol1.appendChild(stdId);
                studentAttend++;
                stdId.style.fontSize = "20px";
                if (placeCount%groups[0] == 0) {  //check to see if we need a new row
                    groupDown = groupDown + 50;
                    groupLeft = 0;
                }
                $( "#" + divName ).animate({
                    left: ( 00 + groupLeft) + "px",
                    top: (100 + groupDown) + "px"
                }, 300 );
                groupLeft = groupLeft + 120;   // keep moving the names over
                placeCount++;
            } else {
                var stdId = document.getElementById(divName);
                stdId.parentNode.id = "studentCol1";
                studentCol1.appendChild(stdId);
                $("#" + divName ).css({
                    left: leftOver + "px",
                    top: "500px",
                } );
                leftOver = leftOver + 110; 
            }
        } 
    };
    
    $("#freezebutton").on("click", function() {
      let groupNumber = $("#freezeGroups").val();
      if (moving == true) {
            clearInterval(interval);
            setTimeout(sort, 1000);
        }
       moving = false;
      
      console.log("Random Group", groupNumber);
    });                
    
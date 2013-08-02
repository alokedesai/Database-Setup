from app import User, db, Skills
data = [
    {
      "name": "Austin Huang", 
      "education": [
        {
          "school": {
            "id": "351573841586647", 
            "name": "Mission San Jose High School"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "34410694953", 
            "name": "De Anza College"
          }, 
          "type": "College"
        }
      ], 
      "id": "501465302"
    }, 
    {
      "name": "Kylan Nieh", 
      "education": [
        {
          "school": {
            "id": "103991312969759", 
            "name": "Mission San Jose High School"
          }, 
          "year": {
            "id": "142963519060927", 
            "name": "2010"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "10111634660", 
            "name": "UC Berkeley"
          }, 
          "year": {
            "id": "143641425651920", 
            "name": "2014"
          }, 
          "type": "College"
        }
      ], 
      "id": "508039156"
    }, 
    {
      "name": "Christine Cheng", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "year": {
            "id": "142963519060927", 
            "name": "2010"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "105517352815443", 
            "name": "California Institute of Technology"
          }, 
          "year": {
            "id": "143641425651920", 
            "name": "2014"
          }, 
          "concentration": [
            {
              "id": "104011699634001", 
              "name": "Chemical Engineering"
            }, 
            {
              "id": "112742452137549", 
              "name": "Sleeping in LC"
            }, 
            {
              "id": "109650445779412", 
              "name": "Minor in English Literature"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "508662523"
    }, 
    {
      "name": "Jennifer Kim", 
      "education": [
        {
          "school": {
            "id": "13917075214", 
            "name": "UC Davis"
          }, 
          "concentration": [
            {
              "id": "392621154125920", 
              "name": "Who Knows"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "509661846"
    }, 
    {
      "name": "Stephanie Yi", 
      "education": [
        {
          "school": {
            "id": "108058285894979", 
            "name": "Irvington High School"
          }, 
          "year": {
            "id": "142963519060927", 
            "name": "2010"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "108047109223278", 
            "name": "University of California, San Diego"
          }, 
          "year": {
            "id": "143641425651920", 
            "name": "2014"
          }, 
          "type": "College"
        }
      ], 
      "id": "511637312"
    }, 
    {
      "name": "Brian Lee", 
      "education": [
        {
          "school": {
            "id": "105495142817230", 
            "name": "University of California, Los Angeles"
          }, 
          "year": {
            "id": "105576766163075", 
            "name": "2015"
          }, 
          "type": "College"
        }
      ], 
      "id": "514213445"
    }, 
    {
      "name": "Joanna Chow", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "year": {
            "id": "115222815248992", 
            "name": "2012"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "10111634660", 
            "name": "UC Berkeley"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "type": "College"
        }
      ], 
      "id": "517010264"
    }, 
    {
      "name": "Jeff Liu", 
      "education": [
        {
          "school": {
            "id": "109748892385588", 
            "name": "Lynbrook High School"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "103127603061486", 
            "name": "Columbia University"
          }, 
          "type": "College"
        }
      ], 
      "id": "520096461"
    }, 
    {
      "name": "Arthur Liou", 
      "id": "520329637"
    }, 
    {
      "name": "Cindy Chao", 
      "id": "520412883"
    }, 
    {
      "name": "AshLey Cochran", 
      "id": "521060563"
    }, 
    {
      "name": "Richard Ducker", 
      "id": "521108497"
    }, 
    {
      "name": "Soo Song", 
      "id": "522963482"
    }, 
    {
      "name": "Edwin Liao", 
      "education": [
        {
          "school": {
            "id": "112235968793130", 
            "name": "Homestead High School"
          }, 
          "year": {
            "id": "142963519060927", 
            "name": "2010"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "106538319376398", 
            "name": "University of California, Berkeley"
          }, 
          "year": {
            "id": "143641425651920", 
            "name": "2014"
          }, 
          "concentration": [
            {
              "id": "105573196144184", 
              "name": "Electrical Engineering and Computer Science"
            }, 
            {
              "id": "107794155922145", 
              "name": "Applied Math"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "523213711"
    }, 
    {
      "name": "Celeste Melamed", 
      "education": [
        {
          "school": {
            "id": "114774318534593", 
            "name": "Lowell High"
          }, 
          "year": {
            "id": "144044875610606", 
            "name": "2011"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "107892159239091", 
            "name": "Harvey Mudd College"
          }, 
          "year": {
            "id": "105576766163075", 
            "name": "2015"
          }, 
          "concentration": [
            {
              "id": "109279729089828", 
              "name": "Physics"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "525105846"
    }, 
    {
      "name": "Alyssa Vargas", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "year": {
            "id": "115222815248992", 
            "name": "2012"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "105454902822165", 
            "name": "San Diego State University"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "type": "College", 
          "classes": [
            {
              "id": "182459431796117", 
              "name": "Class of 2016"
            }
          ]
        }
      ], 
      "id": "526198674"
    }, 
    {
      "name": "Shashank Agrawal", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "134972803193847", 
            "name": "University of Southern California"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "concentration": [
            {
              "id": "186450058076329", 
              "name": "Computer Science and Business"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "527917127"
    },
    {
      "name": "Nithya Thangaraj", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "186291828074120", 
            "name": "Drexel University"
          }, 
          "type": "College", 
          "classes": [
            {
              "id": "182459431796117", 
              "name": "Class of 2016"
            }
          ]
        }
      ], 
      "id": "529007631"
    }, 
    {
      "name": "Marissa Chou", 
      "id": "529162240"
    }, 
    {
      "name": "Justin Jujubee", 
      "education": [
        {
          "school": {
            "id": "114659898545497", 
            "name": "Monta Vista High"
          }, 
          "year": {
            "id": "115222815248992", 
            "name": "2012"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "10111634660", 
            "name": "UC Berkeley"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "type": "College", 
          "classes": [
            {
              "id": "182459431796117", 
              "name": "Class of 2016"
            }
          ]
        }
      ], 
      "id": "529817543"
    }, 
    {
      "name": "Natasha Yeh", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }
      ], 
      "id": "532125387"
    }, 
    {
      "name": "Jonathan Poon", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }
      ], 
      "id": "534858713"
    }, 
    {
      "name": "Mingyu Hu", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "108047109223278", 
            "name": "University of California, San Diego"
          }, 
          "type": "College"
        }
      ], 
      "id": "537349216"
    }, 
    {
      "name": "Tim Nguyen", 
      "id": "538531667"
    }, 
    {
      "name": "Sid Kathiresan", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "7093532993", 
            "name": "Ohlone College"
          }, 
          "concentration": [
            {
              "id": "104076956295773", 
              "name": "Computer Science"
            }
          ], 
          "type": "College"
        }, 
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "College"
        }
      ], 
      "id": "541089316"
    }, 
    {
      "name": "Amanda Su", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "year": {
            "id": "144044875610606", 
            "name": "2011"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "114642418551886", 
            "name": "UC Berkeley"
          }, 
          "year": {
            "id": "105576766163075", 
            "name": "2015"
          }, 
          "type": "College"
        }
      ], 
      "id": "541763413"
    }, 
    {
      "name": "Warren Lee", 
      "education": [
        {
          "school": {
            "id": "109415529078129", 
            "name": "St. George's School"
          }, 
          "year": {
            "id": "293650690709608", 
            "name": "2012"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "102095963164884", 
            "name": "St. Georges"
          }, 
          "year": {
            "id": "118118634930920", 
            "name": "2012"
          }, 
          "type": "High School", 
          "classes": [
            {
              "id": "161878910530139", 
              "name": "Class of 2012"
            }
          ]
        }, 
        {
          "school": {
            "id": "25827817664", 
            "name": "Pomona College"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "type": "College", 
          "classes": [
            {
              "id": "182459431796117", 
              "name": "Class of 2016"
            }
          ]
        }
      ], 
      "id": "542615304"
    }, 
    {
      "name": "Gary Chang", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "year": {
            "id": "144044875610606", 
            "name": "2011"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "105495142817230", 
            "name": "University of California, Los Angeles"
          }, 
          "type": "College"
        }, 
        {
          "school": {
            "id": "112194302140882", 
            "name": "UCLA"
          }, 
          "year": {
            "id": "105576766163075", 
            "name": "2015"
          }, 
          "concentration": [
            {
              "id": "104076956295773", 
              "name": "Computer Science"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "542821352"
    }, 
    {
      "name": "Lisa Chang", 
      "id": "545710775"
    }, 
    {
      "name": "Jesse Pollak", 
      "education": [
        {
          "school": {
            "id": "103946312977698", 
            "name": "Sidwell Friends School"
          }, 
          "year": {
            "id": "201638419856163", 
            "name": "2011"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "103756122996046", 
            "name": "Pomona College"
          }, 
          "year": {
            "id": "105576766163075", 
            "name": "2015"
          }, 
          "type": "College"
        }
      ], 
      "id": "546570578"
    }, 
    {
      "name": "Rebecca Tsai", 
      "id": "546833752"
    }, 
    {
      "name": "Jason Jin", 
      "education": [
        {
          "school": {
            "id": "109748892385588", 
            "name": "Lynbrook High School"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "108069125888094", 
            "name": "Johns Hopkins University"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "type": "College"
        }
      ], 
      "id": "547099063"
    }, 
    {
      "name": "Tammy Tseng", 
      "id": "547844794"
    }, 
    {
      "name": "Michael Z Hwang", 
      "education": [
        {
          "school": {
            "id": "111796055506221", 
            "name": "Leland High"
          }, 
          "year": {
            "id": "201638419856163", 
            "name": "2011"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "10111634660", 
            "name": "UC Berkeley"
          }, 
          "concentration": [
            {
              "id": "108507619171523", 
              "name": "Psychology"
            }, 
            {
              "id": "112936425387489", 
              "name": "Music"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "548159017"
    }, 
    {
      "name": "Obadiah Wright", 
      "education": [
        {
          "school": {
            "id": "112040008807941", 
            "name": "Abraham Lincoln High School"
          }, 
          "year": {
            "id": "115222815248992", 
            "name": "2012"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "44880301202", 
            "name": "Bard College Conservatory of Music"
          }, 
          "year": {
            "id": "532490046771314", 
            "name": "2017"
          }, 
          "concentration": [
            {
              "id": "109823779047223", 
              "name": "Music Composition"
            }, 
            {
              "id": "108384569189012", 
              "name": "Sociology"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "549856617"
    }, 
    {
      "name": "Anthony Kang", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "100526673914", 
            "name": "Purdue University"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "type": "College"
        }
      ], 
      "id": "551893021"
    }, 
    {
      "name": "Tony Hung", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School", 
          "classes": [
            {
              "id": "188918704461958", 
              "name": "2012"
            }
          ]
        }, 
        {
          "school": {
            "id": "110161269012286", 
            "name": "Uc santa cruz"
          }, 
          "type": "College", 
          "classes": [
            {
              "id": "188918704461958", 
              "name": "2012"
            }
          ]
        }
      ], 
      "id": "553016597"
    }, 
    {
      "name": "Tiffany Leong", 
      "id": "553270001"
    }, 
    {
      "name": "Kenta Akaogi", 
      "id": "553300959"
    }, 
    {
      "name": "Daniel Chiou", 
      "education": [
        {
          "school": {
            "id": "109195492439397", 
            "name": "Rangitoto College"
          }, 
          "year": {
            "id": "144044875610606", 
            "name": "2011"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "114595089593", 
            "name": "The University of Auckland"
          }, 
          "year": {
            "id": "425383927542719", 
            "name": "2017"
          }, 
          "concentration": [
            {
              "id": "126269330778473", 
              "name": "Bachelor of Medicine and Bachelor of Surgery (MBChB)"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "553303915"
    }, 
    {
      "name": "Thomas Denq", 
      "id": "555386536"
    }, 
    {
      "name": "Rohan Chandra", 
      "education": [
        {
          "school": {
            "id": "108331145854226", 
            "name": "Harker School"
          }, 
          "year": {
            "id": "120960561375312", 
            "name": "2013"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "140998521533", 
            "name": "Brown University"
          }, 
          "year": {
            "id": "532490046771314", 
            "name": "2017"
          }, 
          "type": "College"
        }
      ], 
      "id": "560196631"
    }, 
    {
      "name": "David Nam", 
      "education": [
        {
          "school": {
            "id": "114659898545497", 
            "name": "Monta Vista High"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "6099747981", 
            "name": "Amherst College"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "type": "College"
        }
      ], 
      "id": "560768470"
    }, 
    {
      "name": "Jennifer Xu", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "103127603061486", 
            "name": "Columbia University"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "concentration": [
            {
              "id": "104011699634001", 
              "name": "Chemical Engineering"
            }, 
            {
              "id": "106240626078926", 
              "name": "Pre-med"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "560943838"
    }, 
    {
      "name": "Joshua Michael", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "111854795497606", 
            "name": "University of Southern California"
          }, 
          "type": "College"
        }
      ], 
      "id": "561847310"
    }, 
    {
      "name": "Jeremy Chua", 
      "id": "562695715"
    }, 
    {
      "name": "Angela Chen", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }
      ], 
      "id": "562872309"
    }, 
    {
      "name": "Grant Lam", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "112199395458691", 
            "name": "University of California, Davis"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "concentration": [
            {
              "id": "104076956295773", 
              "name": "Computer Science"
            }, 
            {
              "id": "107638212592128", 
              "name": "Applied Mathematics"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "566074785"
    }, 
    {
      "name": "Lakshmi Subbaraj", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School", 
          "classes": [
            {
              "id": "161878910530139", 
              "name": "Class of 2012"
            }
          ]
        }, 
        {
          "school": {
            "id": "126533127390327", 
            "name": "Massachusetts Institute of Technology (MIT)"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "type": "College", 
          "classes": [
            {
              "id": "182459431796117", 
              "name": "Class of 2016"
            }
          ]
        }
      ], 
      "id": "566253364"
    }, 
    {
      "name": "Wells Lin", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "year": {
            "id": "118118634930920", 
            "name": "2012"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "100526673914", 
            "name": "Purdue University"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "type": "College"
        }
      ], 
      "id": "566353682"
    }, 
    {
      "name": "Leah Tsao", 
      "education": [
        {
          "school": {
            "id": "108058285894979", 
            "name": "Irvington High School"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "109363495748584", 
            "name": "University of California, Santa Cruz"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "type": "College"
        }
      ], 
      "id": "566747754"
    }, 
    {
      "name": "Leslie Chan", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School", 
          "classes": [
            {
              "id": "161878910530139", 
              "name": "Class of 2012"
            }
          ]
        }
      ], 
      "id": "566761913"
    }, 
    {
      "name": "Diane Yang", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "112112152139559", 
            "name": "Maryland Institute College of Art"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "concentration": [
            {
              "id": "183210538384753", 
              "name": "Art/Graphic Design"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "566772665"
    }, 
    {
      "name": "Stepfanie Lam", 
      "education": [
        {
          "school": {
            "id": "103991312969759", 
            "name": "Mission San Jose High School"
          }, 
          "type": "High School"
        }
      ], 
      "id": "566907097"
    }, 
    {
      "name": "Monica Chitre", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "year": {
            "id": "143018465715205", 
            "name": "2000"
          }, 
          "type": "High School", 
          "classes": [
            {
              "id": "188918704461958", 
              "name": "2012"
            }
          ]
        }
      ], 
      "id": "567202882"
    }, 
    {
      "name": "Nicholas Murphy", 
      "education": [
        {
          "school": {
            "id": "105953446110885", 
            "name": "Berkeley High"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "103756122996046", 
            "name": "Pomona College"
          }, 
          "year": {
            "id": "138879996141011", 
            "name": "2013"
          }, 
          "concentration": [
            {
              "id": "106104499421077", 
              "name": "Molecular Biology"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "567281403"
    }, 
    {
      "name": "Caroline Dang", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "year": {
            "id": "118118634930920", 
            "name": "2012"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "106266172744997", 
            "name": "University of the Pacific"
          }, 
          "type": "College", 
          "classes": [
            {
              "id": "108860105858706", 
              "name": "2018"
            }
          ]
        }
      ], 
      "id": "567393796"
    }, 
    {
      "name": "Vyas Ramasubramani", 
      "education": [
        {
          "school": {
            "id": "109748892385588", 
            "name": "Lynbrook High School"
          }, 
          "year": {
            "id": "136328419721520", 
            "name": "2009"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "18058830773", 
            "name": "Princeton University"
          }, 
          "year": {
            "id": "138879996141011", 
            "name": "2013"
          }, 
          "type": "College"
        }
      ], 
      "id": "567730776"
    }, 
    {
      "name": "Larry Zhong", 
      "education": [
        {
          "school": {
            "id": "103746222996806", 
            "name": "Western Reserve Academy"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "103119943060893", 
            "name": "Claremont McKenna College"
          }, 
          "type": "College"
        }
      ], 
      "id": "568861720"
    }, 
    {
      "name": "Linda Shih", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "122150409780", 
            "name": "UC San Diego"
          }, 
          "concentration": [
            {
              "id": "104076956295773", 
              "name": "Computer Science"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "571187757"
    }, 
    {
      "name": "Kenny Chin", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "112795212068138", 
            "name": "Washington University in St. Louis"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "type": "College"
        }
      ], 
      "id": "571234857"
    }, 
    {
      "name": "Yicheng Sun", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "year": {
            "id": "115222815248992", 
            "name": "2012"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "18058830773", 
            "name": "Princeton University"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "type": "College"
        }
      ], 
      "id": "571257948"
    }, 
    {
      "name": "Anthony Chen", 
      "id": "571259890"
    }, 
    {
      "name": "William Kim", 
      "education": [
        {
          "school": {
            "id": "6192688417", 
            "name": "Stanford University"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School", 
          "classes": [
            {
              "id": "161878910530139", 
              "name": "Class of 2012"
            }
          ]
        }, 
        {
          "school": {
            "id": "6192688417", 
            "name": "Stanford University"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "type": "College"
        }
      ], 
      "id": "571733881"
    }, 
    {
      "name": "Harrison Goodall", 
      "education": [
        {
          "school": {
            "id": "109419089084152", 
            "name": "Ponte Vedra High School"
          }, 
          "type": "High School", 
          "classes": [
            {
              "id": "188918704461958", 
              "name": "2012"
            }
          ]
        }, 
        {
          "school": {
            "id": "103756122996046", 
            "name": "Pomona College"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "type": "College"
        }
      ], 
      "id": "574126836"
    }, 
    {
      "name": "Gianni Graham", 
      "education": [
        {
          "school": {
            "id": "103946312977698", 
            "name": "Sidwell Friends School"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "103756122996046", 
            "name": "Pomona College"
          }, 
          "year": {
            "id": "105576766163075", 
            "name": "2015"
          }, 
          "concentration": [
            {
              "id": "104083339627297", 
              "name": "Neuroscience"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "574315798"
    }, 
    {
      "name": "Budi Salvatore Rpz", 
      "education": [
        {
          "school": {
            "id": "108599439170797", 
            "name": "D.S. Senanayake College"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "106057006101053", 
            "name": "Evony"
          }, 
          "type": "College"
        }, 
        {
          "school": {
            "id": "108139219213848", 
            "name": "University of Sri Jayewardenepura"
          }, 
          "degree": {
            "id": "152440614809772", 
            "name": "BSc"
          }, 
          "year": {
            "id": "136328419721520", 
            "name": "2009"
          }, 
          "type": "Graduate School", 
          "classes": [
            {
              "id": "126244620759699", 
              "name": "2nd Lower!"
            }
          ]
        }
      ], 
      "id": "574744383"
    }, 
    {
      "name": "Kevin Hou", 
      "education": [
        {
          "school": {
            "id": "108058285894979", 
            "name": "Irvington High School"
          }, 
          "year": {
            "id": "115222815248992", 
            "name": "2012"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "112271455455353", 
            "name": "San Jose State University"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "concentration": [
            {
              "id": "104076956295773", 
              "name": "Computer Science"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "580199399"
    }, 
    {
      "name": "Ray Kuo", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "year": {
            "id": "144044875610606", 
            "name": "2011"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "108181769210460", 
            "name": "Orange Coast College"
          }, 
          "year": {
            "id": "143641425651920", 
            "name": "2014"
          }, 
          "concentration": [
            {
              "id": "108271415859752", 
              "name": "Mechanical Engineering"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "581018967"
    }, 
    {
      "name": "Winston Young", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "year": {
            "id": "144044875610606", 
            "name": "2011"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "28972094743", 
            "name": "University of the Pacific"
          }, 
          "year": {
            "id": "105576766163075", 
            "name": "2015"
          }, 
          "concentration": [
            {
              "id": "198864013459878", 
              "name": "Pre-Dental"
            }, 
            {
              "id": "180590625326316", 
              "name": "BA Music"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "581610438"
    }, 
    {
      "name": "Kelly Freitas Berbereia", 
      "id": "583995275"
    }, 
    {
      "name": "Amal Abraham", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School", 
          "classes": [
            {
              "id": "188918704461958", 
              "name": "2012"
            }
          ]
        }, 
        {
          "school": {
            "id": "107888572565045", 
            "name": "University of California, Santa Barbara"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "type": "College"
        }
      ], 
      "id": "584433365"
    }, 
    {
      "name": "Tammy Lian", 
      "id": "584673828"
    }, 
    {
      "name": "Ronald Kwan", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "year": {
            "id": "115222815248992", 
            "name": "2012"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "10111634660", 
            "name": "UC Berkeley"
          }, 
          "concentration": [
            {
              "id": "104076956295773", 
              "name": "Computer Science"
            }, 
            {
              "id": "103966102974293", 
              "name": "Mathematics"
            }, 
            {
              "id": "108227809204607", 
              "name": "Statistics"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "585335189"
    }, 
    {
      "name": "Kabir Gill", 
      "education": [
        {
          "school": {
            "id": "108271019195309", 
            "name": "Gunn High School"
          }, 
          "year": {
            "id": "115222815248992", 
            "name": "2012"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "93768131177", 
            "name": "Washington University in St. Louis"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "type": "College"
        }
      ], 
      "id": "587989987"
    }, 
    {
      "name": "William Leu", 
      "education": [
        {
          "school": {
            "id": "103991312969759", 
            "name": "Mission San Jose High School"
          }, 
          "year": {
            "id": "115222815248992", 
            "name": "2012"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "107888572565045", 
            "name": "University of California, Santa Barbara"
          }, 
          "type": "College"
        }, 
        {
          "school": {
            "id": "106461396056372", 
            "name": "UCSB"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "type": "College"
        }
      ], 
      "id": "588057494"
    }, 
    {
      "name": "Victoria Chang", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "year": {
            "id": "118118634930920", 
            "name": "2012"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "113123972034419", 
            "name": "San Francisco State University"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "type": "College"
        }
      ], 
      "id": "588602742"
    }, 
    {
      "name": "Kevin Guan", 
      "id": "588933678"
    }, 
    {
      "name": "Albert Chuang", 
      "education": [
        {
          "school": {
            "id": "103991312969759", 
            "name": "Mission San Jose High School"
          }, 
          "year": {
            "id": "115222815248992", 
            "name": "2012"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "76026534155", 
            "name": "San Francisco Paramedic Association"
          }, 
          "year": {
            "id": "143641425651920", 
            "name": "2014"
          }, 
          "concentration": [
            {
              "id": "201690396512559", 
              "name": "EMT-Paramedic"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "589390697"
    }, 
    {
      "name": "Austin Wang", 
      "education": [
        {
          "school": {
            "id": "112734332072619", 
            "name": "Palo Alto High School"
          }, 
          "year": {
            "id": "201638419856163", 
            "name": "2011"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "11360325957", 
            "name": "UCLA"
          }, 
          "year": {
            "id": "105576766163075", 
            "name": "2015"
          }, 
          "type": "College"
        }
      ], 
      "id": "589523827"
    }, 
    {
      "name": "Sarah Lee", 
      "education": [
        {
          "school": {
            "id": "113176078692436", 
            "name": "San Francisco School of the Arts"
          }, 
          "year": {
            "id": "136328419721520", 
            "name": "2009"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "108531479171922", 
            "name": "Indiana University"
          }, 
          "year": {
            "id": "138879996141011", 
            "name": "2013"
          }, 
          "concentration": [
            {
              "id": "197950240215577", 
              "name": "Music Performance"
            }
          ], 
          "type": "College"
        }, 
        {
          "school": {
            "id": "324666917640158", 
            "name": "San Francisco Conservatory of Music"
          }, 
          "degree": {
            "id": "125810140829321", 
            "name": "Masters of Music"
          }, 
          "concentration": [
            {
              "id": "101059339972919", 
              "name": "Viola Performance"
            }
          ], 
          "type": "Graduate School"
        }
      ], 
      "id": "591248451"
    }, 
    {
      "name": "Kevin Jiang", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "year": {
            "id": "118118634930920", 
            "name": "2012"
          }, 
          "type": "High School", 
          "classes": [
            {
              "id": "188918704461958", 
              "name": "2012"
            }
          ]
        }, 
        {
          "school": {
            "id": "93415311269", 
            "name": "University of Minnesota"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "type": "College", 
          "classes": [
            {
              "id": "182459431796117", 
              "name": "Class of 2016"
            }
          ]
        }
      ], 
      "id": "592253724"
    }, 
    {
      "name": "Nealay Vasavda", 
      "id": "592708859"
    }, 
    {
      "name": "Jonothan Yuan", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "year": {
            "id": "115222815248992", 
            "name": "2012"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "103256838688", 
            "name": "New York University"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "concentration": [
            {
              "id": "113957928616304", 
              "name": "World Domination"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "592918579"
    }, 
    {
      "name": "Justin Chen", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "10111634660", 
            "name": "UC Berkeley"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "concentration": [
            {
              "id": "104011699634001", 
              "name": "Chemical Engineering"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "593013509"
    }, 
    {
      "name": "Joshua Tsubaki Wu", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "year": {
            "id": "118118634930920", 
            "name": "2012"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "114642418551886", 
            "name": "UC Berkeley"
          }, 
          "concentration": [
            {
              "id": "115163685247948", 
              "name": "Electrical Engineering and Computer Sciences"
            }
          ], 
          "type": "College"
        }, 
        {
          "school": {
            "id": "109521289074413", 
            "name": "University of California, Berkeley College of Engineering"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "concentration": [
            {
              "id": "115163685247948", 
              "name": "Electrical Engineering and Computer Sciences"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "593238881"
    }, 
    {
      "name": "Esther Hsu", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "104094579626449", 
            "name": "Acalanes High School"
          }, 
          "type": "High School"
        }
      ], 
      "id": "593696858"
    }, 
    {
      "name": "Ho Kwong", 
      "id": "594383260"
    }, 
    {
      "name": "Roger Chen", 
      "education": [
        {
          "school": {
            "id": "103991312969759", 
            "name": "Mission San Jose High School"
          }, 
          "year": {
            "id": "144044875610606", 
            "name": "2011"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "6192688417", 
            "name": "Stanford University"
          }, 
          "year": {
            "id": "105576766163075", 
            "name": "2015"
          }, 
          "concentration": [
            {
              "id": "104076956295773", 
              "name": "Computer Science"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "595242153"
    }, 
    {
      "name": "Kanon Lee", 
      "education": [
        {
          "school": {
            "id": "108384185849770", 
            "name": "Albany High School"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "104072539630538", 
            "name": "Holy Names University"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "type": "College"
        }
      ], 
      "id": "598278003"
    }, 
    {
      "name": "Brandon Chen", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "108417049180372", 
            "name": "Rhode Island School of Design"
          }, 
          "type": "College"
        }
      ], 
      "id": "599150663"
    }, 
    {
      "name": "Emily Hsu", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School", 
          "classes": [
            {
              "id": "188918704461958", 
              "name": "2012"
            }
          ]
        }, 
        {
          "school": {
            "id": "11360325957", 
            "name": "UCLA"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "type": "College", 
          "classes": [
            {
              "id": "170481426331222", 
              "name": "2016", 
              "with": [
                {
                  "id": "785460120", 
                  "name": "Maryanne Liu"
                }
              ]
            }
          ]
        }
      ], 
      "id": "599369922"
    }, 
    {
      "name": "Ophelia Ding", 
      "education": [
        {
          "school": {
            "id": "108034402563741", 
            "name": "Cupertino High"
          }, 
          "year": {
            "id": "138879996141011", 
            "name": "2013"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "108047109223278", 
            "name": "University of California, San Diego"
          }, 
          "type": "College"
        }
      ], 
      "id": "599976978"
    }, 
    {
      "name": "Lori Donnelly", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "year": {
            "id": "144044875610606", 
            "name": "2011"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "109551572397323", 
            "name": "University of Michigan"
          }, 
          "year": {
            "id": "143641425651920", 
            "name": "2014"
          }, 
          "concentration": [
            {
              "id": "140402959357080", 
              "name": "Cell and Molecular Biology"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "600613486"
    }, 
    {
      "name": "Sophia Wang", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School", 
          "classes": [
            {
              "id": "161878910530139", 
              "name": "Class of 2012"
            }
          ]
        }, 
        {
          "school": {
            "id": "108047109223278", 
            "name": "University of California, San Diego"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "concentration": [
            {
              "id": "111990655542663", 
              "name": "Physiology and Neuroscience"
            }
          ], 
          "type": "College", 
          "classes": [
            {
              "id": "182459431796117", 
              "name": "Class of 2016"
            }
          ]
        }
      ], 
      "id": "600676036"
    }, 
    {
      "name": "Melody Shieh", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "10111634660", 
            "name": "UC Berkeley"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "type": "College"
        }
      ], 
      "id": "601444275"
    }, 
    {
      "name": "Benjamin Liu", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "year": {
            "id": "144044875610606", 
            "name": "2011"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "10111634660", 
            "name": "UC Berkeley"
          }, 
          "year": {
            "id": "105576766163075", 
            "name": "2015"
          }, 
          "concentration": [
            {
              "id": "104076956295773", 
              "name": "Computer Science"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "603823299"
    }, 
    {
      "name": "Mallika Gargeya", 
      "id": "604649485"
    }, 
    {
      "name": "Kevin Nguyen", 
      "education": [
        {
          "school": {
            "id": "107693532593304", 
            "name": "White Station High School"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "106257739406306", 
            "name": "Christian Brothers High School"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "25827817664", 
            "name": "Pomona College"
          }, 
          "type": "College"
        }
      ], 
      "id": "605797877"
    }, 
    {
      "name": "Walter Hsiang", 
      "id": "607215756"
    }, 
    {
      "name": "Mengfei Li", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "year": {
            "id": "118118634930920", 
            "name": "2012"
          }, 
          "type": "High School"
        }
      ], 
      "id": "610568723"
    }, 
    {
      "name": "Daryl Chang", 
      "education": [
        {
          "school": {
            "id": "104154589622349", 
            "name": "Saratoga High School"
          }, 
          "year": {
            "id": "201638419856163", 
            "name": "2011"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "6192688417", 
            "name": "Stanford University"
          }, 
          "year": {
            "id": "105576766163075", 
            "name": "2015"
          }, 
          "type": "College"
        }
      ], 
      "id": "610630966"
    }, 
    {
      "name": "Alex Lei Qin", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "year": {
            "id": "115222815248992", 
            "name": "2012"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "228401243342", 
            "name": "Northwestern University"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "type": "College"
        }
      ], 
      "id": "610638913"
    }, 
    {
      "name": "Kristi Tran", 
      "education": [
        {
          "school": {
            "id": "108021559232773", 
            "name": "St. Francis High School"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "134972803193847", 
            "name": "University of Southern California"
          }, 
          "concentration": [
            {
              "id": "104083339627297", 
              "name": "Neuroscience"
            }
          ], 
          "type": "College", 
          "classes": [
            {
              "id": "182459431796117", 
              "name": "Class of 2016"
            }
          ]
        }
      ], 
      "id": "611606115"
    }, 
    {
      "name": "Polly Ma", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "year": {
            "id": "118118634930920", 
            "name": "2012"
          }, 
          "type": "High School", 
          "classes": [
            {
              "id": "188918704461958", 
              "name": "2012"
            }
          ]
        }, 
        {
          "school": {
            "id": "108069125888094", 
            "name": "Johns Hopkins University"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "concentration": [
            {
              "id": "109353535758331", 
              "name": "Biomedical Engineering"
            }
          ], 
          "type": "College", 
          "classes": [
            {
              "id": "170481426331222", 
              "name": "2016"
            }
          ]
        }
      ], 
      "id": "616255554"
    }, 
    {
      "name": "Dylan King", 
      "education": [
        {
          "school": {
            "id": "103991312969759", 
            "name": "Mission San Jose High School"
          }, 
          "year": {
            "id": "115222815248992", 
            "name": "2012"
          }, 
          "type": "High School", 
          "classes": [
            {
              "id": "161878910530139", 
              "name": "Class of 2012"
            }
          ]
        }, 
        {
          "school": {
            "id": "122150409780", 
            "name": "UC San Diego"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "concentration": [
            {
              "id": "104076956295773", 
              "name": "Computer Science"
            }
          ], 
          "type": "College", 
          "classes": [
            {
              "id": "182459431796117", 
              "name": "Class of 2016"
            }
          ]
        }
      ], 
      "id": "616533229"
    }, 
    {
      "name": "Irene Wang", 
      "education": [
        {
          "school": {
            "id": "275087292600061", 
            "name": "Cupertino High School"
          }, 
          "type": "High School", 
          "classes": [
            {
              "id": "241170439258676", 
              "name": "11th Grade Tutorial", 
              "with": [
                {
                  "id": "100001105561518", 
                  "name": "Leo Jian-Li Wang"
                }
              ], 
              "from": {
                "id": "100001105561518", 
                "name": "Leo Jian-Li Wang"
              }
            }
          ]
        }, 
        {
          "school": {
            "id": "6391532964", 
            "name": "California Institute of Technology"
          }, 
          "type": "College"
        }
      ], 
      "id": "616944059"
    }, 
    {
      "name": "Maya Ramachandran", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "126533127390327", 
            "name": "Massachusetts Institute of Technology (MIT)"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "type": "College"
        }
      ], 
      "id": "617547999"
    }, 
    {
      "name": "Jin Bai", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School", 
          "classes": [
            {
              "id": "188918704461958", 
              "name": "2012"
            }
          ]
        }, 
        {
          "school": {
            "id": "100526673914", 
            "name": "Purdue University"
          }, 
          "type": "College", 
          "classes": [
            {
              "id": "182459431796117", 
              "name": "Class of 2016"
            }
          ]
        }
      ], 
      "id": "618204736"
    }, 
    {
      "name": "Annie Gu", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }
      ], 
      "id": "618584304"
    }, 
    {
      "name": "Alexandra Ruff", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "61441666906", 
            "name": "Vanderbilt University"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "type": "College"
        }
      ], 
      "id": "619187934"
    }, 
    {
      "name": "Kim Nguyen", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "107888572565045", 
            "name": "University of California, Santa Barbara"
          }, 
          "type": "College"
        }
      ], 
      "id": "620161453"
    }, 
    {
      "name": "Vincent Huang", 
      "education": [
        {
          "school": {
            "id": "108034402563741", 
            "name": "Cupertino High"
          }, 
          "year": {
            "id": "144044875610606", 
            "name": "2011"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "108069125888094", 
            "name": "Johns Hopkins University"
          }, 
          "year": {
            "id": "105576766163075", 
            "name": "2015"
          }, 
          "type": "College"
        }, 
        {
          "school": {
            "id": "108034402563741", 
            "name": "Cupertino High"
          }, 
          "year": {
            "id": "144044875610606", 
            "name": "2011"
          }, 
          "type": "College"
        }
      ], 
      "id": "624408464"
    }, 
    {
      "name": "Jeremy Pathmanabhan", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "134972803193847", 
            "name": "University of Southern California"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "concentration": [
            {
              "id": "103724069666039", 
              "name": "Biochemistry"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "624572631"
    }, 
    {
      "name": "Kevin Zhao", 
      "education": [
        {
          "school": {
            "id": "108034402563741", 
            "name": "Cupertino High"
          }, 
          "year": {
            "id": "144044875610606", 
            "name": "2011"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "112331748780082", 
            "name": "Northwestern University"
          }, 
          "type": "College"
        }, 
        {
          "school": {
            "id": "228401243342", 
            "name": "Northwestern University"
          }, 
          "year": {
            "id": "105576766163075", 
            "name": "2015"
          }, 
          "concentration": [
            {
              "id": "197844203574978", 
              "name": "Bassoon Performance"
            }, 
            {
              "id": "106258142742717", 
              "name": "Materials Science & Engineering"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "624595983"
    }, 
    {
      "name": "Monica Kriselle Macabitas", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "112073472144959", 
            "name": "Washington High School"
          }, 
          "type": "High School"
        }
      ], 
      "id": "625816956"
    }, 
    {
      "name": "Max Jiao", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "year": {
            "id": "118118634930920", 
            "name": "2012"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "122150409780", 
            "name": "UC San Diego"
          }, 
          "type": "College"
        }
      ], 
      "id": "629136830"
    }, 
    {
      "name": "Param Bhatter", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School", 
          "classes": [
            {
              "id": "161878910530139", 
              "name": "Class of 2012", 
              "with": [
                {
                  "id": "746338651", 
                  "name": "Henry Hwaun"
                }
              ], 
              "from": {
                "id": "746338651", 
                "name": "Henry Hwaun"
              }
            }
          ]
        }, 
        {
          "school": {
            "id": "104328202999303", 
            "name": "UC San Diego"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "concentration": [
            {
              "id": "193935540636448", 
              "name": "Bioengineering"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "630727434"
    }, 
    {
      "name": "Kevin Zhai", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "6192688417", 
            "name": "Stanford University"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "type": "College"
        }
      ], 
      "id": "631012667"
    }, 
    {
      "name": "Edward Wang", 
      "id": "631421132"
    }, 
    {
      "name": "Lucy Guo", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "110718578953431", 
            "name": "Amador Valley High"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "110098575679764", 
            "name": "Foothill High"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "170657132947108", 
            "name": "Carnegie Mellon School of Computer Science - SCS"
          }, 
          "type": "College"
        }, 
        {
          "school": {
            "id": "7133766387", 
            "name": "Carnegie Mellon University"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "concentration": [
            {
              "id": "104076956295773", 
              "name": "Computer Science"
            }, 
            {
              "id": "104096132959364", 
              "name": "Business"
            }
          ], 
          "type": "College", 
          "classes": [
            {
              "id": "219763834746006", 
              "name": "Computer science"
            }, 
            {
              "id": "198492473509855", 
              "name": "Electrical and Computer Eng.", 
              "with": [
                {
                  "id": "687697924", 
                  "name": "Krino Pan"
                }, 
                {
                  "id": "1676958512", 
                  "name": "Scott Reid"
                }, 
                {
                  "id": "1412855133", 
                  "name": "Manuel Diaz Corrada"
                }, 
                {
                  "id": "698221653", 
                  "name": "Karen Wang"
                }, 
                {
                  "id": "1152710844", 
                  "name": "Everett Hu"
                }, 
                {
                  "id": "1090287281", 
                  "name": "Estefania Ortiz"
                }, 
                {
                  "id": "533667106", 
                  "name": "Aramael Andres Pena-Alcantara"
                }
              ]
            }
          ]
        }
      ], 
      "id": "633454537"
    }, 
    {
      "name": "Catherine Dugan", 
      "education": [
        {
          "school": {
            "id": "112882282059975", 
            "name": "Lexington High School"
          }, 
          "year": {
            "id": "144044875610606", 
            "name": "2011"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "105686252798585", 
            "name": "The Mountain School"
          }, 
          "year": {
            "id": "144044875610606", 
            "name": "2011"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "103756122996046", 
            "name": "Pomona College"
          }, 
          "year": {
            "id": "105576766163075", 
            "name": "2015"
          }, 
          "type": "College"
        }
      ], 
      "id": "633980578"
    }, 
    {
      "name": "Shannon Lubetich", 
      "id": "635172723"
    }, 
    {
      "name": "Alex Wang", 
      "education": [
        {
          "school": {
            "id": "108058285894979", 
            "name": "Irvington High School"
          }, 
          "year": {
            "id": "201638419856163", 
            "name": "2011"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "6192688417", 
            "name": "Stanford University"
          }, 
          "year": {
            "id": "105576766163075", 
            "name": "2015"
          }, 
          "concentration": [
            {
              "id": "104076956295773", 
              "name": "Computer Science"
            }, 
            {
              "id": "180333162008749", 
              "name": "Music - Piano Performance"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "635203434"
    }, 
    {
      "name": "Emily Chang", 
      "education": [
        {
          "school": {
            "id": "109748892385588", 
            "name": "Lynbrook High School"
          }, 
          "year": {
            "id": "115222815248992", 
            "name": "2012"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "103756122996046", 
            "name": "Pomona College"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "type": "College", 
          "classes": [
            {
              "id": "327495810612400", 
              "name": "Pomona College Class of 2016"
            }
          ]
        }
      ], 
      "id": "635355386"
    }, 
    {
      "name": "Jessica Chiu", 
      "education": [
        {
          "school": {
            "id": "112235968793130", 
            "name": "Homestead High School"
          }, 
          "type": "High School", 
          "classes": [
            {
              "id": "188918704461958", 
              "name": "2012"
            }
          ]
        }, 
        {
          "school": {
            "id": "10111634660", 
            "name": "UC Berkeley"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "type": "College"
        }
      ], 
      "id": "636084501"
    }, 
    {
      "name": "Timmy Tang", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }
      ], 
      "id": "638968925"
    }, 
    {
      "name": "Xaria Kirtikar", 
      "id": "639953116"
    }, 
    {
      "name": "Jonathan Sirsir", 
      "education": [
        {
          "school": {
            "id": "111796055506221", 
            "name": "Leland High"
          }, 
          "type": "High School", 
          "classes": [
            {
              "id": "161878910530139", 
              "name": "Class of 2012"
            }
          ]
        }, 
        {
          "school": {
            "id": "28972094743", 
            "name": "University of the Pacific"
          }, 
          "concentration": [
            {
              "id": "198864013459878", 
              "name": "Pre-Dental"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "641057755"
    }, 
    {
      "name": "Rodney Tang", 
      "education": [
        {
          "school": {
            "id": "134972803193847", 
            "name": "University of Southern California"
          }, 
          "type": "College"
        }, 
        {
          "school": {
            "id": "107888572565045", 
            "name": "University of California, Santa Barbara"
          }, 
          "type": "College"
        }
      ], 
      "id": "644672646"
    }, 
    {
      "name": "Max Li Walter Isenberg", 
      "education": [
        {
          "school": {
            "id": "108331145854226", 
            "name": "Harker School"
          }, 
          "type": "High School", 
          "classes": [
            {
              "id": "188918704461958", 
              "name": "2012"
            }
          ]
        }, 
        {
          "school": {
            "id": "72646999723", 
            "name": "The Wharton School"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "type": "College"
        }, 
        {
          "school": {
            "id": "98508878775", 
            "name": "University of Pennsylvania"
          }, 
          "concentration": [
            {
              "id": "109532545739630", 
              "name": "Engineering"
            }, 
            {
              "id": "104096132959364", 
              "name": "Business"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "647502508"
    }, 
    {
      "name": "Ben Cohen", 
      "education": [
        {
          "school": {
            "id": "111971465487045", 
            "name": "Moorestown High School"
          }, 
          "type": "High School", 
          "classes": [
            {
              "id": "161878910530139", 
              "name": "Class of 2012"
            }
          ]
        }, 
        {
          "school": {
            "id": "103756122996046", 
            "name": "Pomona College"
          }, 
          "concentration": [
            {
              "id": "109275475757504", 
              "name": "International Relations"
            }, 
            {
              "id": "112624162082677", 
              "name": "Russian"
            }
          ], 
          "type": "College", 
          "classes": [
            {
              "id": "182459431796117", 
              "name": "Class of 2016"
            }
          ]
        }
      ], 
      "id": "651812944"
    }, 
    {
      "name": "Alanna Rice", 
      "education": [
        {
          "school": {
            "id": "111964282150016", 
            "name": "Los Altos High School"
          }, 
          "year": {
            "id": "115222815248992", 
            "name": "2012"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "161718535966", 
            "name": "Chapman University"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "concentration": [
            {
              "id": "106113389419954", 
              "name": "English Literature"
            }, 
            {
              "id": "111997592208204", 
              "name": "Integrated Educational Studies"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "653189351"
    }, 
    {
      "name": "Gurman Shoker", 
      "id": "654837217"
    }, 
    {
      "name": "Menglin Ruan", 
      "id": "660286634"
    }, 
    {
      "name": "Chang Chun Hwang", 
      "education": [
        {
          "school": {
            "id": "109748892385588", 
            "name": "Lynbrook High School"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "112194302140882", 
            "name": "UCLA"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "concentration": [
            {
              "id": "104076956295773", 
              "name": "Computer Science"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "663881984"
    }, 
    {
      "name": "Tim Zhang", 
      "education": [
        {
          "school": {
            "id": "111796055506221", 
            "name": "Leland High"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "111851825501258", 
            "name": "NYU"
          }, 
          "type": "College"
        }, 
        {
          "school": {
            "id": "103256838688", 
            "name": "New York University"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "type": "College"
        }
      ], 
      "id": "663974224"
    }, 
    {
      "name": "Lisa Doong", 
      "id": "665558780"
    }, 
    {
      "name": "Chelsea Dass", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "year": {
            "id": "144044875610606", 
            "name": "2011"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "108619679169559", 
            "name": "UC Davis"
          }, 
          "year": {
            "id": "105576766163075", 
            "name": "2015"
          }, 
          "type": "College"
        }, 
        {
          "school": {
            "id": "112199395458691", 
            "name": "University of California, Davis"
          }, 
          "year": {
            "id": "105576766163075", 
            "name": "2015"
          }, 
          "type": "College", 
          "classes": [
            {
              "id": "128303600571030", 
              "name": "of 2015", 
              "with": [
                {
                  "id": "100000376771051", 
                  "name": "Lorena Ramirez"
                }
              ], 
              "from": {
                "id": "100000376771051", 
                "name": "Lorena Ramirez"
              }
            }
          ]
        }
      ], 
      "id": "666561227"
    }, 
    {
      "name": "Christopher Lee", 
      "education": [
        {
          "school": {
            "id": "104154589622349", 
            "name": "Saratoga High School"
          }, 
          "year": {
            "id": "120960561375312", 
            "name": "2013"
          }, 
          "type": "High School", 
          "classes": [
            {
              "id": "145006845560677", 
              "name": "2013"
            }
          ]
        }, 
        {
          "school": {
            "id": "8829726273", 
            "name": "University of Washington"
          }, 
          "type": "College", 
          "classes": [
            {
              "id": "134288253303575", 
              "name": "2017"
            }
          ]
        }
      ], 
      "id": "667459670"
    }, 
    {
      "name": "Simone Cadoppi", 
      "education": [
        {
          "school": {
            "id": "113176078692436", 
            "name": "San Francisco School of the Arts"
          }, 
          "year": {
            "id": "144044875610606", 
            "name": "2011"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "113123972034419", 
            "name": "San Francisco State University"
          }, 
          "year": {
            "id": "105576766163075", 
            "name": "2015"
          }, 
          "type": "College"
        }
      ], 
      "id": "667809202"
    }, 
    {
      "name": "Haebin Liew", 
      "education": [
        {
          "school": {
            "id": "103991312969759", 
            "name": "Mission San Jose High School"
          }, 
          "year": {
            "id": "115222815248992", 
            "name": "2012"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "108047109223278", 
            "name": "University of California, San Diego"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "type": "College"
        }
      ], 
      "id": "668919702"
    }, 
    {
      "name": "Winnie Ding", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "107363709293503", 
            "name": "University of California, Irvine"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "concentration": [
            {
              "id": "101059339972919", 
              "name": "Viola Performance"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "670103707"
    }, 
    {
      "name": "Stephen Hou", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "year": {
            "id": "144044875610606", 
            "name": "2011"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "107727705916498", 
            "name": "University of California, Riverside"
          }, 
          "year": {
            "id": "105576766163075", 
            "name": "2015"
          }, 
          "concentration": [
            {
              "id": "140586009339198", 
              "name": "Business Economics"
            }, 
            {
              "id": "197950240215577", 
              "name": "Music Performance"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "674978847"
    }, 
    {
      "name": "Prithvi Ramesh", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "year": {
            "id": "144044875610606", 
            "name": "2011"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "163536409904", 
            "name": "University of Illinois at Urbana-Champaign"
          }, 
          "year": {
            "id": "105576766163075", 
            "name": "2015"
          }, 
          "concentration": [
            {
              "id": "114379705245469", 
              "name": "Electrical and Computer Engineering"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "676173708"
    }, 
    {
      "name": "David Chang", 
      "education": [
        {
          "school": {
            "id": "104154589622349", 
            "name": "Saratoga High School"
          }, 
          "year": {
            "id": "201638419856163", 
            "name": "2011"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "10111634660", 
            "name": "UC Berkeley"
          }, 
          "year": {
            "id": "105576766163075", 
            "name": "2015"
          }, 
          "type": "College"
        }
      ], 
      "id": "676942590"
    }, 
    {
      "name": "Katelyn Liu", 
      "id": "677603053"
    }, 
    {
      "name": "Vincent Lin", 
      "education": [
        {
          "school": {
            "id": "51449109465", 
            "name": "Lowell High School"
          }, 
          "type": "High School"
        }
      ], 
      "id": "677696567"
    }, 
    {
      "name": "Allison Hwang", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "year": {
            "id": "115222815248992", 
            "name": "2012"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "192609620649", 
            "name": "The University of Chicago"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "concentration": [
            {
              "id": "179398022102115", 
              "name": "Economics and Computer Science"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "677828827"
    }, 
    {
      "name": "Calvin Chen", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "115348195145712", 
            "name": "National Experimental"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "106538319376398", 
            "name": "University of California, Berkeley"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "type": "College"
        }
      ], 
      "id": "679133732"
    }, 
    {
      "name": "Justin Juan", 
      "education": [
        {
          "school": {
            "id": "103991312969759", 
            "name": "Mission San Jose High School"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "104073636296325", 
            "name": "Brown University"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "concentration": [
            {
              "id": "109353535758331", 
              "name": "Biomedical Engineering"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "681501728"
    }, 
    {
      "name": "Gary Hua", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "13917075214", 
            "name": "UC Davis"
          }, 
          "type": "College"
        }, 
        {
          "school": {
            "id": "112199395458691", 
            "name": "University of California, Davis"
          }, 
          "type": "College"
        }
      ], 
      "id": "682396248"
    }, 
    {
      "name": "Emily Hou", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School", 
          "classes": [
            {
              "id": "145006845560677", 
              "name": "2013"
            }
          ]
        }, 
        {
          "school": {
            "id": "28972094743", 
            "name": "University of the Pacific"
          }, 
          "type": "College"
        }
      ], 
      "id": "682418335"
    }, 
    {
      "name": "Theo Ma", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "year": {
            "id": "144044875610606", 
            "name": "2011"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "112194302140882", 
            "name": "UCLA"
          }, 
          "year": {
            "id": "105576766163075", 
            "name": "2015"
          }, 
          "concentration": [
            {
              "id": "179178312123764", 
              "name": "Viola"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "682609879"
    }, 
    {
      "name": "Kevin He", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "108047109223278", 
            "name": "University of California, San Diego"
          }, 
          "type": "College"
        }, 
        {
          "school": {
            "id": "104328202999303", 
            "name": "UC San Diego"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "concentration": [
            {
              "id": "104076956295773", 
              "name": "Computer Science"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "683207032"
    }, 
    {
      "name": "Candice Suh", 
      "education": [
        {
          "school": {
            "id": "104154589622349", 
            "name": "Saratoga High School"
          }, 
          "year": {
            "id": "138879996141011", 
            "name": "2013"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "11360325957", 
            "name": "UCLA"
          }, 
          "type": "College"
        }
      ], 
      "id": "683667912"
    }, 
    {
      "name": "Eric Chen", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School", 
          "classes": [
            {
              "id": "188918704461958", 
              "name": "2012"
            }
          ]
        }, 
        {
          "school": {
            "id": "107888572565045", 
            "name": "University of California, Santa Barbara"
          }, 
          "concentration": [
            {
              "id": "104076956295773", 
              "name": "Computer Science"
            }
          ], 
          "type": "College", 
          "classes": [
            {
              "id": "182459431796117", 
              "name": "Class of 2016"
            }
          ]
        }
      ], 
      "id": "688688732"
    }, 
    {
      "name": "Anastassia Yurievna Gorvitovskaia", 
      "education": [
        {
          "school": {
            "id": "115000781848912", 
            "name": "Lawson Middle School"
          }, 
          "year": {
            "id": "141778012509913", 
            "name": "2008"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "275087292600061", 
            "name": "Cupertino High School"
          }, 
          "year": {
            "id": "118118634930920", 
            "name": "2012"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "108034402563741", 
            "name": "Cupertino High"
          }, 
          "year": {
            "id": "115222815248992", 
            "name": "2012"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "140998521533", 
            "name": "Brown University"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "concentration": [
            {
              "id": "177727508939224", 
              "name": "PLME"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "690944387"
    }, 
    {
      "name": "Jordeen Chang", 
      "id": "691122773"
    }, 
    {
      "name": "Adam Law", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "year": {
            "id": "118118634930920", 
            "name": "2012"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "107888572565045", 
            "name": "University of California, Santa Barbara"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "type": "College"
        }
      ], 
      "id": "691230798"
    }, 
    {
      "name": "Aryana Yee", 
      "id": "691617855"
    }, 
    {
      "name": "Sindhu Gnanasambandan", 
      "education": [
        {
          "school": {
            "id": "115000781848912", 
            "name": "Lawson Middle School"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "108034402563741", 
            "name": "Cupertino High"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "275087292600061", 
            "name": "Cupertino High School"
          }, 
          "type": "High School", 
          "classes": [
            {
              "id": "107512149278840", 
              "name": "Journalism", 
              "with": [
                {
                  "id": "594874457", 
                  "name": "Anthony Kao"
                }
              ], 
              "from": {
                "id": "594874457", 
                "name": "Anthony Kao"
              }
            }
          ]
        }, 
        {
          "school": {
            "id": "108877405802697", 
            "name": "University of Chicago"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "type": "College"
        }
      ], 
      "id": "691644185"
    }, 
    {
      "name": "Elly Lin", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "10111634660", 
            "name": "UC Berkeley"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "type": "College"
        }
      ], 
      "id": "691761018"
    }, 
    {
      "name": "Sydney Ha", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "24965068856", 
            "name": "UC Irvine"
          }, 
          "type": "College"
        }
      ], 
      "id": "691801616"
    }, 
    {
      "name": "Malinda Cheung", 
      "education": [
        {
          "school": {
            "id": "13917075214", 
            "name": "UC Davis"
          }, 
          "concentration": [
            {
              "id": "104011699634001", 
              "name": "Chemical Engineering"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "691816213"
    }, 
    {
      "name": "Aaron Yang", 
      "education": [
        {
          "school": {
            "id": "103991312969759", 
            "name": "Mission San Jose High School"
          }, 
          "year": {
            "id": "115222815248992", 
            "name": "2012"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "112199395458691", 
            "name": "University of California, Davis"
          }, 
          "type": "College"
        }
      ], 
      "id": "691868915"
    }, 
    {
      "name": "Amanda Trinh", 
      "education": [
        {
          "school": {
            "id": "152634244768294", 
            "name": "Notre Dame High School"
          }, 
          "year": {
            "id": "201638419856163", 
            "name": "2011"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "111854795497606", 
            "name": "University of Southern California"
          }, 
          "year": {
            "id": "105576766163075", 
            "name": "2015"
          }, 
          "concentration": [
            {
              "id": "108654845832522", 
              "name": "Business Administration"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "692876341"
    }, 
    {
      "name": "Khalid Dhanani", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "107888572565045", 
            "name": "University of California, Santa Barbara"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "type": "College"
        }
      ], 
      "id": "693610814"
    }, 
    {
      "name": "Kevin Chung", 
      "education": [
        {
          "school": {
            "id": "106136996084734", 
            "name": "Mercer Island High School"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "103756122996046", 
            "name": "Pomona College"
          }, 
          "year": {
            "id": "105576766163075", 
            "name": "2015"
          }, 
          "concentration": [
            {
              "id": "104083339627297", 
              "name": "Neuroscience"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "693842695"
    }, 
    {
      "name": "Warren Kwong", 
      "education": [
        {
          "school": {
            "id": "108331145854226", 
            "name": "Harker School"
          }, 
          "year": {
            "id": "144044875610606", 
            "name": "2011"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "46577622172", 
            "name": "USC Thornton School of Music"
          }, 
          "concentration": [
            {
              "id": "181069671930741", 
              "name": "Music Industry"
            }
          ], 
          "type": "College"
        }, 
        {
          "school": {
            "id": "111854795497606", 
            "name": "University of Southern California"
          }, 
          "type": "College"
        }
      ], 
      "id": "697450593"
    }, 
    {
      "name": "Alice Timken", 
      "education": [
        {
          "school": {
            "id": "108384185849770", 
            "name": "Albany High School"
          }, 
          "year": {
            "id": "118118634930920", 
            "name": "2012"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "103756122996046", 
            "name": "Pomona College"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "type": "College"
        }
      ], 
      "id": "699289229"
    }, 
    {
      "name": "Tyler Hsieh", 
      "education": [
        {
          "school": {
            "id": "112235968793130", 
            "name": "Homestead High School"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "11360325957", 
            "name": "UCLA"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "concentration": [
            {
              "id": "109439469082967", 
              "name": "Music Education"
            }, 
            {
              "id": "189140651108439", 
              "name": "Clarinet Performance"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "699982570"
    }, 
    {
      "name": "Michelle Won", 
      "education": [
        {
          "school": {
            "id": "104154589622349", 
            "name": "Saratoga High School"
          }, 
          "year": {
            "id": "138879996141011", 
            "name": "2013"
          }, 
          "type": "High School"
        }
      ], 
      "id": "700272754"
    }, 
    {
      "name": "Sean Chung", 
      "education": [
        {
          "school": {
            "id": "108098629224708", 
            "name": "Northwood High School"
          }, 
          "year": {
            "id": "141778012509913", 
            "name": "2008"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "103756122996046", 
            "name": "Pomona College"
          }, 
          "year": {
            "id": "115222815248992", 
            "name": "2012"
          }, 
          "concentration": [
            {
              "id": "104083339627297", 
              "name": "Neuroscience"
            }, 
            {
              "id": "112936425387489", 
              "name": "Music"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "701189223"
    }, 
    {
      "name": "Felic Wang", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }
      ], 
      "id": "702357054"
    }, 
    {
      "name": "Allison Tong", 
      "education": [
        {
          "school": {
            "id": "103991312969759", 
            "name": "Mission San Jose High School"
          }, 
          "year": {
            "id": "115222815248992", 
            "name": "2012"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "17767109610", 
            "name": "University of Miami"
          }, 
          "type": "College"
        }
      ], 
      "id": "702746532"
    }, 
    {
      "name": "Vishal Shea", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "83086245170", 
            "name": "University of Colorado Boulder"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "concentration": [
            {
              "id": "108220405864767", 
              "name": "Aerospace Engineering"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "704292370"
    }, 
    {
      "name": "David Wu", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "351573841586647", 
            "name": "Mission San Jose High School"
          }, 
          "year": {
            "id": "142963519060927", 
            "name": "2010"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "106563469381382", 
            "name": "UC Irvine"
          }, 
          "type": "College"
        }, 
        {
          "school": {
            "id": "107363709293503", 
            "name": "University of California, Irvine"
          }, 
          "year": {
            "id": "143641425651920", 
            "name": "2014"
          }, 
          "concentration": [
            {
              "id": "109279729089828", 
              "name": "Physics"
            }, 
            {
              "id": "112936425387489", 
              "name": "Music"
            }, 
            {
              "id": "105470119487701", 
              "name": "Education"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "704317192"
    }, 
    {
      "name": "Eric Xu", 
      "education": [
        {
          "school": {
            "id": "109748892385588", 
            "name": "Lynbrook High School"
          }, 
          "year": {
            "id": "138879996141011", 
            "name": "2013"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "18058830773", 
            "name": "Princeton University"
          }, 
          "year": {
            "id": "532490046771314", 
            "name": "2017"
          }, 
          "type": "College", 
          "classes": [
            {
              "id": "179039122137632", 
              "name": "Class of 2017"
            }
          ]
        }
      ], 
      "id": "706191994"
    }, 
    {
      "name": "Blaze Lee", 
      "education": [
        {
          "school": {
            "id": "108271019195309", 
            "name": "Gunn High School"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "140998521533", 
            "name": "Brown University"
          }, 
          "year": {
            "id": "185588044800194", 
            "name": "2017"
          }, 
          "concentration": [
            {
              "id": "103999666303070", 
              "name": "Medicine"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "708169587"
    }, 
    {
      "name": "Kyle Qian", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "year": {
            "id": "120960561375312", 
            "name": "2013"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "6192688417", 
            "name": "Stanford University"
          }, 
          "year": {
            "id": "532490046771314", 
            "name": "2017"
          }, 
          "type": "College"
        }
      ], 
      "id": "708627265"
    }, 
    {
      "name": "Jessica Leong", 
      "education": [
        {
          "school": {
            "id": "106614486041161", 
            "name": "Piedmont Hills High"
          }, 
          "year": {
            "id": "140617569303679", 
            "name": "2007"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "103108179728954", 
            "name": "West Valley College"
          }, 
          "year": {
            "id": "136328419721520", 
            "name": "2009"
          }, 
          "concentration": [
            {
              "id": "107709299252611", 
              "name": "Architecture"
            }
          ], 
          "type": "College"
        }, 
        {
          "school": {
            "id": "111014978922837", 
            "name": "Boston Architectural"
          }, 
          "year": {
            "id": "138879996141011", 
            "name": "2013"
          }, 
          "concentration": [
            {
              "id": "107709299252611", 
              "name": "Architecture"
            }
          ], 
          "type": "College"
        }, 
        {
          "school": {
            "id": "112080292151282", 
            "name": "Boston Architectural College"
          }, 
          "type": "Graduate School"
        }
      ], 
      "id": "709236900"
    }, 
    {
      "name": "Heather Tang", 
      "education": [
        {
          "school": {
            "id": "103991312969759", 
            "name": "Mission San Jose High School"
          }, 
          "type": "High School"
        }
      ], 
      "id": "712084594"
    }, 
    {
      "name": "Lily Xu", 
      "education": [
        {
          "school": {
            "id": "103991312969759", 
            "name": "Mission San Jose High School"
          }, 
          "year": {
            "id": "115222815248992", 
            "name": "2012"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "114620441888143", 
            "name": "NYU Stern"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "concentration": [
            {
              "id": "104096132959364", 
              "name": "Business"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "712235151"
    }, 
    {
      "name": "Chris Ce Ce Lo", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "111821125502507", 
            "name": "none yet"
          }, 
          "type": "College"
        }, 
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "College"
        }
      ], 
      "id": "712298967"
    }, 
    {
      "name": "Aaron Wong", 
      "id": "712864008"
    }, 
    {
      "name": "Tiffany Jang", 
      "education": [
        {
          "school": {
            "id": "108331145854226", 
            "name": "Harker School"
          }, 
          "year": {
            "id": "115222815248992", 
            "name": "2012"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "112194302140882", 
            "name": "UCLA"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "type": "College"
        }
      ], 
      "id": "713559749"
    }, 
    {
      "name": "Desiree Xu", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "year": {
            "id": "144044875610606", 
            "name": "2011"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "7133766387", 
            "name": "Carnegie Mellon University"
          }, 
          "year": {
            "id": "105576766163075", 
            "name": "2015"
          }, 
          "type": "College"
        }
      ], 
      "id": "713661254"
    }, 
    {
      "name": "Kyle Gerner", 
      "education": [
        {
          "school": {
            "id": "110941085596968", 
            "name": "The King's Academy"
          }, 
          "year": {
            "id": "144044875610606", 
            "name": "2011"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "112545315425325", 
            "name": "Santa Clara University"
          }, 
          "concentration": [
            {
              "id": "113496838660747", 
              "name": "Chemistry"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "713720786"
    }, 
    {
      "name": "Angela Wang", 
      "id": "714030412"
    }, 
    {
      "name": "Evan Yao", 
      "education": [
        {
          "school": {
            "id": "108331145854226", 
            "name": "Harker School"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "10111634660", 
            "name": "UC Berkeley"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "concentration": [
            {
              "id": "151139964942329", 
              "name": "EECS"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "714837889"
    }, 
    {
      "name": "Kevin Yang", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "College"
        }
      ], 
      "id": "715299701"
    }, 
    {
      "name": "Regina Ahn", 
      "education": [
        {
          "school": {
            "id": "108271019195309", 
            "name": "Gunn High School"
          }, 
          "year": {
            "id": "144044875610606", 
            "name": "2011"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "11360325957", 
            "name": "UCLA"
          }, 
          "year": {
            "id": "105576766163075", 
            "name": "2015"
          }, 
          "concentration": [
            {
              "id": "104083339627297", 
              "name": "Neuroscience"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "719037145"
    }, 
    {
      "name": "Natalie Hall", 
      "education": [
        {
          "school": {
            "id": "111796055506221", 
            "name": "Leland High"
          }, 
          "year": {
            "id": "142963519060927", 
            "name": "2010"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "104073636296325", 
            "name": "Brown University"
          }, 
          "year": {
            "id": "143641425651920", 
            "name": "2014"
          }, 
          "concentration": [
            {
              "id": "109314462420288", 
              "name": "Biology"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "725700586"
    }, 
    {
      "name": "Hirut Mamo", 
      "education": [
        {
          "school": {
            "id": "110142779015405", 
            "name": "Shorewood High School"
          }, 
          "year": {
            "id": "136328419721520", 
            "name": "2009"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "103756122996046", 
            "name": "Pomona College"
          }, 
          "year": {
            "id": "138879996141011", 
            "name": "2013"
          }, 
          "concentration": [
            {
              "id": "191617390859013", 
              "name": "Politics & Psychology"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "728082740"
    }, 
    {
      "name": "Morgan Yucel", 
      "id": "728332712"
    }, 
    {
      "name": "Erin Chen", 
      "id": "730990412"
    }, 
    {
      "name": "Liz Lee", 
      "education": [
        {
          "school": {
            "id": "114659898545497", 
            "name": "Monta Vista High"
          }, 
          "year": {
            "id": "138879996141011", 
            "name": "2013"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "10111634660", 
            "name": "UC Berkeley"
          }, 
          "type": "College"
        }
      ], 
      "id": "731002143"
    }, 
    {
      "name": "Leon Leung", 
      "education": [
        {
          "school": {
            "id": "103991312969759", 
            "name": "Mission San Jose High School"
          }, 
          "year": {
            "id": "142963519060927", 
            "name": "2010"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "351573841586647", 
            "name": "Mission San Jose High School"
          }, 
          "year": {
            "id": "142963519060927", 
            "name": "2010"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "103175909766842", 
            "name": "University of California, Berkeley"
          }, 
          "type": "College"
        }, 
        {
          "school": {
            "id": "10111634660", 
            "name": "UC Berkeley"
          }, 
          "year": {
            "id": "143641425651920", 
            "name": "2014"
          }, 
          "concentration": [
            {
              "id": "108180979203954", 
              "name": "Economics"
            }, 
            {
              "id": "110739222287627", 
              "name": "Accounting"
            }
          ], 
          "type": "College"
        }, 
        {
          "school": {
            "id": "106513019385948", 
            "name": "UCSC"
          }, 
          "concentration": [
            {
              "id": "189589017728648", 
              "name": "Business Management Economics"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "731746635"
    }, 
    {
      "name": "Ritty Zhai", 
      "education": [
        {
          "school": {
            "id": "115000781848912", 
            "name": "Lawson Middle School"
          }, 
          "year": {
            "id": "141778012509913", 
            "name": "2008"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "110357042320781", 
            "name": "Archbishop Mitty"
          }, 
          "year": {
            "id": "115222815248992", 
            "name": "2012"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "103127603061486", 
            "name": "Columbia University"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "type": "College"
        }
      ], 
      "id": "735143102"
    }, 
    {
      "name": "Alex Peng", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }
      ], 
      "id": "735613800"
    }, 
    {
      "name": "Elvin Wong", 
      "education": [
        {
          "school": {
            "id": "109642382395535", 
            "name": "Monta Vista High School"
          }, 
          "year": {
            "id": "293650690709608", 
            "name": "2012"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "106179239412557", 
            "name": "De Anza College"
          }, 
          "year": {
            "id": "120960561375312", 
            "name": "2013"
          }, 
          "concentration": [
            {
              "id": "154113941309526", 
              "name": "Transfer Credits"
            }
          ], 
          "type": "College"
        }, 
        {
          "school": {
            "id": "20697868961", 
            "name": "Boston University"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "concentration": [
            {
              "id": "112259292124160", 
              "name": "Advertising"
            }, 
            {
              "id": "113336252010022", 
              "name": "Marketing"
            }, 
            {
              "id": "104045469631213", 
              "name": "Political Science"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "735769813"
    }, 
    {
      "name": "Stephen Chen", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "24743274366", 
            "name": "California Polytechnic State University (Cal Poly)"
          }, 
          "type": "College"
        }
      ], 
      "id": "735928662"
    }, 
    {
      "name": "Rey Tang", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "year": {
            "id": "143641425651920", 
            "name": "2014"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "College"
        }
      ], 
      "id": "738412445"
    }, 
    {
      "name": "Anthony Cao", 
      "education": [
        {
          "school": {
            "id": "112235968793130", 
            "name": "Homestead High School"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "11360325957", 
            "name": "UCLA"
          }, 
          "year": {
            "id": "105576766163075", 
            "name": "2015"
          }, 
          "concentration": [
            {
              "id": "104076956295773", 
              "name": "Computer Science"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "738523652"
    }, 
    {
      "name": "Alex Krishnan", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "year": {
            "id": "136328419721520", 
            "name": "2009"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "109363495748584", 
            "name": "University of California, Santa Cruz"
          }, 
          "year": {
            "id": "138879996141011", 
            "name": "2013"
          }, 
          "concentration": [
            {
              "id": "164342496949537", 
              "name": "French Horn Performance"
            }, 
            {
              "id": "112377098773944", 
              "name": "Computer Engineering"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "738777493"
    }, 
    {
      "name": "Jon Kan", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "year": {
            "id": "143641425651920", 
            "name": "2014"
          }, 
          "type": "High School"
        }
      ], 
      "id": "740943501"
    }, 
    {
      "name": "Reilly Tamer", 
      "education": [
        {
          "school": {
            "id": "110773788946272", 
            "name": "Mountain View High"
          }, 
          "year": {
            "id": "144044875610606", 
            "name": "2011"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "28972094743", 
            "name": "University of the Pacific"
          }, 
          "year": {
            "id": "105576766163075", 
            "name": "2015"
          }, 
          "concentration": [
            {
              "id": "109439469082967", 
              "name": "Music Education"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "741207880"
    }, 
    {
      "name": "Himaja Doddapaneni", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School", 
          "classes": [
            {
              "id": "188918704461958", 
              "name": "2012"
            }
          ]
        }
      ], 
      "id": "741281391"
    }, 
    {
      "name": "Kevin Wu", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School", 
          "classes": [
            {
              "id": "188918704461958", 
              "name": "2012"
            }
          ]
        }, 
        {
          "school": {
            "id": "10111634660", 
            "name": "UC Berkeley"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "concentration": [
            {
              "id": "193935540636448", 
              "name": "Bioengineering"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "741720679"
    }, 
    {
      "name": "Rebecca Tso", 
      "education": [
        {
          "school": {
            "id": "105572882808621", 
            "name": "Cupertino High School"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "100526673914", 
            "name": "Purdue University"
          }, 
          "type": "College"
        }
      ], 
      "id": "743079629"
    }, 
    {
      "name": "Andersen Chang", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "year": {
            "id": "118118634930920", 
            "name": "2012"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "7133766387", 
            "name": "Carnegie Mellon University"
          }, 
          "type": "College"
        }
      ], 
      "id": "743673632"
    }, 
    {
      "name": "Siddarth Sen", 
      "id": "743748329"
    }, 
    {
      "name": "Jerry Lee", 
      "education": [
        {
          "school": {
            "id": "102096756499212", 
            "name": "Irvine High"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "25827817664", 
            "name": "Pomona College"
          }, 
          "type": "College"
        }
      ], 
      "id": "744670278"
    }, 
    {
      "name": "Henry Hwaun", 
      "education": [
        {
          "school": {
            "id": "101860189870845", 
            "name": ""
          }, 
          "year": {
            "id": "137616982934053", 
            "name": "2006"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "year": {
            "id": "115222815248992", 
            "name": "2012"
          }, 
          "type": "High School", 
          "classes": [
            {
              "id": "161878910530139", 
              "name": "Class of 2012", 
              "with": [
                {
                  "id": "630727434", 
                  "name": "Param Bhatter"
                }
              ]
            }
          ]
        }, 
        {
          "school": {
            "id": "10111634660", 
            "name": "UC Berkeley"
          }, 
          "type": "College"
        }
      ], 
      "id": "746338651"
    }, 
    {
      "name": "Amos Liou", 
      "education": [
        {
          "school": {
            "id": "112235968793130", 
            "name": "Homestead High School"
          }, 
          "year": {
            "id": "144044875610606", 
            "name": "2011"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "103778026327507", 
            "name": "University of Rochester"
          }, 
          "year": {
            "id": "105576766163075", 
            "name": "2015"
          }, 
          "concentration": [
            {
              "id": "103724069666039", 
              "name": "Biochemistry"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "748410578"
    }, 
    {
      "name": "Peter Kim", 
      "education": [
        {
          "school": {
            "id": "108058285894979", 
            "name": "Irvington High School"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "10111634660", 
            "name": "UC Berkeley"
          }, 
          "year": {
            "id": "143641425651920", 
            "name": "2014"
          }, 
          "concentration": [
            {
              "id": "104076956295773", 
              "name": "Computer Science"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "750480920"
    }, 
    {
      "name": "Richard Ying", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "year": {
            "id": "118118634930920", 
            "name": "2012"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "115883931822842", 
            "name": "UC San Diego Jacobs School of Engineering"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "concentration": [
            {
              "id": "104076956295773", 
              "name": "Computer Science"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "753667975"
    }, 
    {
      "name": "Merry Mou", 
      "id": "755034552"
    }, 
    {
      "name": "Mindy Lai", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "6711658857", 
            "name": "The Ohio State University"
          }, 
          "type": "College"
        }
      ], 
      "id": "757116513"
    }, 
    {
      "name": "Charles Guan", 
      "id": "758392153"
    }, 
    {
      "name": "Tim Lin", 
      "id": "758435584"
    }, 
    {
      "name": "Gordon Tom", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "year": {
            "id": "138879996141011", 
            "name": "2013"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "28972094743", 
            "name": "University of the Pacific"
          }, 
          "concentration": [
            {
              "id": "196975100315038", 
              "name": "Pre-Pharmacy"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "759082592"
    }, 
    {
      "name": "Otto Wong", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "10111634660", 
            "name": "UC Berkeley"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "type": "College"
        }
      ], 
      "id": "760140370"
    }, 
    {
      "name": "Zeeshan Pirzada", 
      "education": [
        {
          "school": {
            "id": "351573841586647", 
            "name": "Mission San Jose High School"
          }, 
          "year": {
            "id": "118118634930920", 
            "name": "2012"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "105495142817230", 
            "name": "University of California, Los Angeles"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "type": "College"
        }
      ], 
      "id": "766068801"
    }, 
    {
      "name": "Witisada Wattananimitgul", 
      "education": [
        {
          "school": {
            "id": "108055682555657", 
            "name": "Chandler High School"
          }, 
          "year": {
            "id": "118118634930920", 
            "name": "2012"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "103756122996046", 
            "name": "Pomona College"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "type": "College"
        }
      ], 
      "id": "766502849"
    }, 
    {
      "name": "Tim Kang", 
      "id": "769785362"
    }, 
    {
      "name": "Curran Sinha", 
      "education": [
        {
          "school": {
            "id": "108271019195309", 
            "name": "Gunn High School"
          }, 
          "year": {
            "id": "138879996141011", 
            "name": "2013"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "8570160131", 
            "name": "Cornell University"
          }, 
          "type": "College"
        }
      ], 
      "id": "779954672"
    }, 
    {
      "name": "Atisheel Kak", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "year": {
            "id": "144044875610606", 
            "name": "2011"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "100526673914", 
            "name": "Purdue University"
          }, 
          "year": {
            "id": "143641425651920", 
            "name": "2014"
          }, 
          "concentration": [
            {
              "id": "188405807858656", 
              "name": "Biological Engineering"
            }, 
            {
              "id": "140757425987253", 
              "name": "Food Process Engineering"
            }
          ], 
          "type": "College"
        }, 
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "year": {
            "id": "201638419856163", 
            "name": "2011"
          }, 
          "type": "College"
        }
      ], 
      "id": "782899736"
    }, 
    {
      "name": "Maryanne Liu", 
      "id": "785460120"
    }, 
    {
      "name": "James Vu", 
      "id": "786770586"
    }, 
    {
      "name": "Daniyal Aleem", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }
      ], 
      "id": "788999463"
    }, 
    {
      "name": "Shannon Pai", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "10111634660", 
            "name": "UC Berkeley"
          }, 
          "type": "College"
        }
      ], 
      "id": "790894643"
    }, 
    {
      "name": "Eugenia Chung", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "year": {
            "id": "144044875610606", 
            "name": "2011"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "13917075214", 
            "name": "UC Davis"
          }, 
          "year": {
            "id": "105576766163075", 
            "name": "2015"
          }, 
          "type": "College"
        }
      ], 
      "id": "791332908"
    },  
    {
      "name": "Brian Wang", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "374809010319", 
            "name": "Yale University"
          }, 
          "type": "College"
        }
      ], 
      "id": "805589476"
    }, 
    {
      "name": "Angela Wu", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School", 
          "classes": [
            {
              "id": "188918704461958", 
              "name": "2012"
            }
          ]
        }, 
        {
          "school": {
            "id": "112271455455353", 
            "name": "San Jose State University"
          }, 
          "type": "College"
        }
      ], 
      "id": "805808150"
    }, 
    {
      "name": "Dorothy Liu", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "year": {
            "id": "115222815248992", 
            "name": "2012"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "28972094743", 
            "name": "University of the Pacific"
          }, 
          "type": "College"
        }
      ], 
      "id": "808698138"
    }, 
    {
      "name": "Justine Liang", 
      "id": "809928269"
    }, 
    {
      "name": "Jason Lau", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "College"
        }
      ], 
      "id": "814605542"
    }, 
    {
      "name": "William Shi", 
      "education": [
        {
          "school": {
            "id": "112185785460576", 
            "name": "Torrey Pines High School"
          }, 
          "year": {
            "id": "144044875610606", 
            "name": "2011"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "16279648193", 
            "name": "Bowdoin College"
          }, 
          "concentration": [
            {
              "id": "103724069666039", 
              "name": "Biochemistry"
            }, 
            {
              "id": "108384569189012", 
              "name": "Sociology"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "817545278"
    }, 
    {
      "name": "Adrienne Chumsta", 
      "education": [
        {
          "school": {
            "id": "114654691885382", 
            "name": "University High School"
          }, 
          "year": {
            "id": "136328419721520", 
            "name": "2009"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "7133766387", 
            "name": "Carnegie Mellon University"
          }, 
          "year": {
            "id": "138879996141011", 
            "name": "2013"
          }, 
          "type": "College"
        }
      ], 
      "id": "817793632"
    }, 
    {
      "name": "Yuni Kay", 
      "education": [
        {
          "school": {
            "id": "162826000426019", 
            "name": ""
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "109260719100477", 
            "name": "Whitney High School"
          }, 
          "year": {
            "id": "201638419856163", 
            "name": "2011"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "110678318959787", 
            "name": "Claremont Colleges"
          }, 
          "type": "College"
        }, 
        {
          "school": {
            "id": "103756122996046", 
            "name": "Pomona College"
          }, 
          "year": {
            "id": "105576766163075", 
            "name": "2015"
          }, 
          "type": "College"
        }
      ], 
      "id": "818969644"
    }, 
    {
      "name": "Myung MG Chi", 
      "education": [
        {
          "school": {
            "id": "109748892385588", 
            "name": "Lynbrook High School"
          }, 
          "year": {
            "id": "120960561375312", 
            "name": "2013"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "10111634660", 
            "name": "UC Berkeley"
          }, 
          "concentration": [
            {
              "id": "105573196144184", 
              "name": "Electrical Engineering and Computer Science"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "823620619"
    }, 
    {
      "name": "Mike Yang", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "11360325957", 
            "name": "UCLA"
          }, 
          "type": "College"
        }, 
        {
          "school": {
            "id": "105495142817230", 
            "name": "University of California, Los Angeles"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "concentration": [
            {
              "id": "109314462420288", 
              "name": "Biology"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "825202355"
    }, 
    {
      "name": "James Chang", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "year": {
            "id": "293650690709608", 
            "name": "2012"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "10111634660", 
            "name": "UC Berkeley"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "type": "College"
        }
      ], 
      "id": "826927339"
    }, 
    {
      "name": "Emily Jang", 
      "id": "829044735"
    }, 
    {
      "name": "Shannon Burns", 
      "education": [
        {
          "school": {
            "id": "116443228365812", 
            "name": "Los Alamos High"
          }, 
          "year": {
            "id": "144044875610606", 
            "name": "2011"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "103756122996046", 
            "name": "Pomona College"
          }, 
          "year": {
            "id": "105576766163075", 
            "name": "2015"
          }, 
          "type": "College"
        }
      ], 
      "id": "832599127"
    }, 
    {
      "name": "Karen Hou", 
      "id": "833235596"
    }, 
    {
      "name": "Daniel James Valentine", 
      "id": "833766169"
    }, 
    {
      "name": "Vincent Tian", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "year": {
            "id": "118118634930920", 
            "name": "2012"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "10111634660", 
            "name": "UC Berkeley"
          }, 
          "type": "College"
        }
      ], 
      "id": "853930233"
    }, 
    {
      "name": "Arthur Shir", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "13917075214", 
            "name": "UC Davis"
          }, 
          "type": "College"
        }
      ], 
      "id": "856009180"
    }, 
    {
      "name": "Allen Peng", 
      "id": "856974500"
    }, 
    {
      "name": "Tian Shi", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }
      ], 
      "id": "857134356"
    }, 
    {
      "name": "Benjamin Gauss", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "112271455455353", 
            "name": "San Jose State University"
          }, 
          "concentration": [
            {
              "id": "110739222287627", 
              "name": "Accounting"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "864205054"
    }, 
    {
      "name": "Sanjna Shukla", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "113618111985274", 
            "name": "Pennsylvania State University"
          }, 
          "type": "College"
        }
      ], 
      "id": "894850252"
    }, 
    {
      "name": "Arash Dehdashty", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }
      ], 
      "id": "894980432"
    }, 
    {
      "name": "Vasilis Dravilas", 
      "id": "895570150"
    }, 
    {
      "name": "Kyle Chen", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "year": {
            "id": "115222815248992", 
            "name": "2012"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "10111634660", 
            "name": "UC Berkeley"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "type": "College"
        }
      ], 
      "id": "896010471"
    }, 
    {
      "name": "Dora Chang", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "year": {
            "id": "115222815248992", 
            "name": "2012"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "102657818085", 
            "name": "University of California, Riverside"
          }, 
          "type": "College"
        }
      ], 
      "id": "896670064"
    }, 
    {
      "name": "Connie Chen", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "134972803193847", 
            "name": "University of Southern California"
          }, 
          "concentration": [
            {
              "id": "110739222287627", 
              "name": "Accounting"
            }
          ], 
          "type": "College", 
          "classes": [
            {
              "id": "182459431796117", 
              "name": "Class of 2016"
            }
          ]
        }
      ], 
      "id": "897120104"
    }, 
    {
      "name": "Arvind Srinivasan", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "163536409904", 
            "name": "University of Illinois at Urbana-Champaign"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "type": "College"
        }, 
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "College"
        }
      ], 
      "id": "1002508709"
    }, 
    {
      "name": "Farris Tang", 
      "id": "1004188321"
    }, 
    {
      "name": "Andrew Licko", 
      "education": [
        {
          "school": {
            "id": "112325088780290", 
            "name": "Junipero Serra High School"
          }, 
          "year": {
            "id": "138879996141011", 
            "name": "2013"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "25855743604", 
            "name": "Indiana University Jacobs School of Music"
          }, 
          "year": {
            "id": "532490046771314", 
            "name": "2017"
          }, 
          "type": "College"
        }
      ], 
      "id": "1004236508"
    }, 
    {
      "name": "Sida Lu", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "year": {
            "id": "118118634930920", 
            "name": "2012"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "134972803193847", 
            "name": "University of Southern California"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "concentration": [
            {
              "id": "166491370064800", 
              "name": "Business Administration/Management"
            }
          ], 
          "type": "College", 
          "classes": [
            {
              "id": "182459431796117", 
              "name": "Class of 2016"
            }
          ]
        }
      ], 
      "id": "1005486085"
    }, 
    {
      "name": "Justin Hang", 
      "education": [
        {
          "school": {
            "id": "104154589622349", 
            "name": "Saratoga High School"
          }, 
          "year": {
            "id": "138879996141011", 
            "name": "2013"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "11360325957", 
            "name": "UCLA"
          }, 
          "year": {
            "id": "532490046771314", 
            "name": "2017"
          }, 
          "type": "College"
        }
      ], 
      "id": "1006103339"
    }, 
    {
      "name": "Lawrence Luo", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "year": {
            "id": "143641425651920", 
            "name": "2014"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "year": {
            "id": "143641425651920", 
            "name": "2014"
          }, 
          "type": "College"
        }
      ], 
      "id": "1006567194"
    }, 
    {
      "name": "Tiffany Keller", 
      "education": [
        {
          "school": {
            "id": "110536458966941", 
            "name": "Castro Valley High"
          }, 
          "year": {
            "id": "118118634930920", 
            "name": "2012"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "24743274366", 
            "name": "California Polytechnic State University (Cal Poly)"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "concentration": [
            {
              "id": "113336252010022", 
              "name": "Marketing"
            }, 
            {
              "id": "112261935460307", 
              "name": "Business Law"
            }, 
            {
              "id": "104096132959364", 
              "name": "Business"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "1007055636"
    }, 
    {
      "name": "Michael Wang", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "107888572565045", 
            "name": "University of California, Santa Barbara"
          }, 
          "type": "College"
        }
      ], 
      "id": "1008694954"
    }, 
    {
      "name": "Kevin Chen", 
      "education": [
        {
          "school": {
            "id": "103991312969759", 
            "name": "Mission San Jose High School"
          }, 
          "year": {
            "id": "118118634930920", 
            "name": "2012"
          }, 
          "type": "High School"
        }
      ], 
      "id": "1009258495"
    }, 
    {
      "name": "Vivek Sudhakar", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School", 
          "classes": [
            {
              "id": "188918704461958", 
              "name": "2012"
            }
          ]
        }, 
        {
          "school": {
            "id": "103721419666144", 
            "name": "University of Pittsburgh"
          }, 
          "concentration": [
            {
              "id": "104083339627297", 
              "name": "Neuroscience"
            }
          ], 
          "type": "College", 
          "classes": [
            {
              "id": "182459431796117", 
              "name": "Class of 2016"
            }
          ]
        }
      ], 
      "id": "1010848398"
    }, 
    {
      "name": "Jasmine Chen", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "year": {
            "id": "115222815248992", 
            "name": "2012"
          }, 
          "type": "High School"
        }
      ], 
      "id": "1011657126"
    }, 
    {
      "name": "Aneesh Natarajan", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "122150409780", 
            "name": "UC San Diego"
          }, 
          "type": "College"
        }
      ], 
      "id": "1012649782"
    }, 
    {
      "name": "Warren Tian", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }
      ], 
      "id": "1013403569"
    }, 
    {
      "name": "Kurt Hamilton", 
      "id": "1015172022"
    }, 
    {
      "name": "Nick Yang", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "year": {
            "id": "115222815248992", 
            "name": "2012"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "110030499019521", 
            "name": "Cal Poly San Luis Obispo"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "type": "College"
        }
      ], 
      "id": "1015954897"
    }, 
    {
      "name": "Jordan Suo", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }
      ], 
      "id": "1020541822"
    }, 
    {
      "name": "Shray Bansal", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "134972803193847", 
            "name": "University of Southern California"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "concentration": [
            {
              "id": "103113796395285", 
              "name": "Kinesiology"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "1024111790"
    }, 
    {
      "name": "Brandon Wong", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "year": {
            "id": "118118634930920", 
            "name": "2012"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "102657818085", 
            "name": "University of California, Riverside"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "concentration": [
            {
              "id": "140586009339198", 
              "name": "Business Economics"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "1032136279"
    }, 
    {
      "name": "Samuel Chen", 
      "education": [
        {
          "school": {
            "id": "102096756499212", 
            "name": "Irvine High"
          }, 
          "type": "High School", 
          "classes": [
            {
              "id": "161878910530139", 
              "name": "Class of 2012"
            }
          ]
        }, 
        {
          "school": {
            "id": "25827817664", 
            "name": "Pomona College"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "type": "College", 
          "classes": [
            {
              "id": "182459431796117", 
              "name": "Class of 2016"
            }
          ]
        }
      ], 
      "id": "1032139321"
    }, 
    {
      "name": "Tasha Tuong", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "year": {
            "id": "142963519060927", 
            "name": "2010"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "110277459002324", 
            "name": "Lee's Summit North"
          }, 
          "year": {
            "id": "115222815248992", 
            "name": "2012"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "156658154449", 
            "name": "UMKC School of Medicine"
          }, 
          "type": "College"
        }
      ], 
      "id": "1033768346"
    }, 
    {
      "name": "Jovian Lam", 
      "id": "1033983282"
    }, 
    {
      "name": "Al Hassani", 
      "education": [
        {
          "school": {
            "id": "108034402563741", 
            "name": "Cupertino High"
          }, 
          "year": {
            "id": "118118634930920", 
            "name": "2012"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "206635849419702", 
            "name": "Purdue University Class of 2016"
          }, 
          "type": "College"
        }
      ], 
      "id": "1036320352"
    }, 
    {
      "name": "Frances Jih", 
      "education": [
        {
          "school": {
            "id": "114659898545497", 
            "name": "Monta Vista High"
          }, 
          "year": {
            "id": "142963519060927", 
            "name": "2010"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "10111634660", 
            "name": "UC Berkeley"
          }, 
          "year": {
            "id": "143641425651920", 
            "name": "2014"
          }, 
          "type": "College"
        }
      ], 
      "id": "1036380895"
    }, 
    {
      "name": "Elaine Tang", 
      "id": "1036381106"
    }, 
    {
      "name": "Eric Ding", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "year": {
            "id": "136328419721520", 
            "name": "2009"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "103256838688", 
            "name": "New York University"
          }, 
          "year": {
            "id": "138879996141011", 
            "name": "2013"
          }, 
          "type": "College"
        }
      ], 
      "id": "1038750592"
    }, 
    {
      "name": "Teddy Fong", 
      "id": "1038750608"
    }, 
    {
      "name": "Paula Burkhardt", 
      "education": [
        {
          "school": {
            "id": "16460270446", 
            "name": "Friends' Central School"
          }, 
          "year": {
            "id": "118118634930920", 
            "name": "2012"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "25827817664", 
            "name": "Pomona College"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "type": "College"
        }, 
        {
          "school": {
            "id": "339133692846772", 
            "name": "Stanford Summer College"
          }, 
          "type": "College"
        }
      ], 
      "id": "1038810163"
    }, 
    {
      "name": "Winnie Chan", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "10111634660", 
            "name": "UC Berkeley"
          }, 
          "type": "College"
        }
      ], 
      "id": "1039615558"
    }, 
    {
      "name": "Ryan Yee", 
      "id": "1041094834"
    }, 
    {
      "name": "Tim Fang", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School", 
          "classes": [
            {
              "id": "188918704461958", 
              "name": "2012"
            }
          ]
        }, 
        {
          "school": {
            "id": "6391532964", 
            "name": "California Institute of Technology"
          }, 
          "concentration": [
            {
              "id": "140129116051987", 
              "name": "Applied and Computational Mathematics"
            }, 
            {
              "id": "155290254526470", 
              "name": "Business Economics and Management"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "1043674846"
    }, 
    {
      "name": "Bryan Cassella", 
      "education": [
        {
          "school": {
            "id": "111964282150016", 
            "name": "Los Altos High School"
          }, 
          "year": {
            "id": "142963519060927", 
            "name": "2010"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "108047109223278", 
            "name": "University of California, San Diego"
          }, 
          "year": {
            "id": "143641425651920", 
            "name": "2014"
          }, 
          "type": "College"
        }
      ], 
      "id": "1044030257"
    }, 
    {
      "name": "Peyton Fonck", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "year": {
            "id": "118118634930920", 
            "name": "2012"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "109706542392483", 
            "name": "University of Washington, Seattle"
          }, 
          "type": "College"
        }
      ], 
      "id": "1044358532"
    }, 
    {
      "name": "Brian Hou", 
      "id": "1046774705"
    }, 
    {
      "name": "Tiffany Wu", 
      "education": [
        {
          "school": {
            "id": "110773788946272", 
            "name": "Mountain View High"
          }, 
          "year": {
            "id": "140617569303679", 
            "name": "2007"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "107363709293503", 
            "name": "University of California, Irvine"
          }, 
          "year": {
            "id": "144044875610606", 
            "name": "2011"
          }, 
          "concentration": [
            {
              "id": "106066639425552", 
              "name": "History"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "1047210301"
    }, 
    {
      "name": "Shreyas Bharadwaj", 
      "education": [
        {
          "school": {
            "id": "281481875236963", 
            "name": "Duke University Class of 2016"
          }, 
          "type": "College"
        }
      ], 
      "id": "1048258274"
    }, 
    {
      "name": "Austin Lau", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "year": {
            "id": "118118634930920", 
            "name": "2012"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "107727705916498", 
            "name": "University of California, Riverside"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "concentration": [
            {
              "id": "112092048806093", 
              "name": "Business Marketing"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "1055174702"
    }, 
    {
      "name": "Michelle Huang", 
      "id": "1055790586"
    }, 
    {
      "name": "Amy Lee", 
      "education": [
        {
          "school": {
            "id": "109748892385588", 
            "name": "Lynbrook High School"
          }, 
          "year": {
            "id": "142963519060927", 
            "name": "2010"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "108047109223278", 
            "name": "University of California, San Diego"
          }, 
          "year": {
            "id": "143641425651920", 
            "name": "2014"
          }, 
          "concentration": [
            {
              "id": "141144965947957", 
              "name": "Psychology/Pre-Med"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "1055790707"
    }, 
    {
      "name": "Dustin Yu", 
      "education": [
        {
          "school": {
            "id": "109748892385588", 
            "name": "Lynbrook High School"
          }, 
          "year": {
            "id": "142963519060927", 
            "name": "2010"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "108047109223278", 
            "name": "University of California, San Diego"
          }, 
          "year": {
            "id": "143641425651920", 
            "name": "2014"
          }, 
          "concentration": [
            {
              "id": "197826393562287", 
              "name": "B.S. Computer Science"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "1055790709"
    }, 
    {
      "name": "Samuel Swei", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "10111634660", 
            "name": "UC Berkeley"
          }, 
          "type": "College"
        }
      ], 
      "id": "1057447264"
    }, 
    {
      "name": "Brian Tang", 
      "education": [
        {
          "school": {
            "id": "104154589622349", 
            "name": "Saratoga High School"
          }, 
          "year": {
            "id": "136328419721520", 
            "name": "2009"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "108047109223278", 
            "name": "University of California, San Diego"
          }, 
          "year": {
            "id": "138879996141011", 
            "name": "2013"
          }, 
          "concentration": [
            {
              "id": "202209776459612", 
              "name": "Cognitive Science with a Specialization in Neuroscience"
            }, 
            {
              "id": "112936425387489", 
              "name": "Music"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "1057890083"
    }, 
    {
      "name": "Audrey Kwong", 
      "education": [
        {
          "school": {
            "id": "108331145854226", 
            "name": "Harker School"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "111854795497606", 
            "name": "University of Southern California"
          }, 
          "year": {
            "id": "201638419856163", 
            "name": "2011"
          }, 
          "concentration": [
            {
              "id": "128845670519714", 
              "name": "Violin Performance"
            }, 
            {
              "id": "200310283317861", 
              "name": "Cinematic Arts"
            }, 
            {
              "id": "181069671930741", 
              "name": "Music Industry"
            }
          ], 
          "type": "College"
        }, 
        {
          "school": {
            "id": "7133766387", 
            "name": "Carnegie Mellon University"
          }, 
          "degree": {
            "id": "186760704696934", 
            "name": "Masters of Arts Management"
          }, 
          "year": {
            "id": "138879996141011", 
            "name": "2013"
          }, 
          "concentration": [
            {
              "id": "128055040596791", 
              "name": "Arts Management"
            }
          ], 
          "type": "Graduate School"
        }
      ], 
      "id": "1063110362"
    }, 
    {
      "name": "Miles Shen", 
      "education": [
        {
          "school": {
            "id": "111980318819469", 
            "name": "Menlo School"
          }, 
          "year": {
            "id": "142963519060927", 
            "name": "2010"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "18058830773", 
            "name": "Princeton University"
          }, 
          "year": {
            "id": "143641425651920", 
            "name": "2014"
          }, 
          "concentration": [
            {
              "id": "106104499421077", 
              "name": "Molecular Biology"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "1063140484"
    }, 
    {
      "name": "Belinda Li", 
      "education": [
        {
          "school": {
            "id": "111797255513490", 
            "name": "Mira Loma High"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "103756122996046", 
            "name": "Pomona College"
          }, 
          "type": "College"
        }
      ], 
      "id": "1063740148"
    }, 
    {
      "name": "Susie Chang", 
      "id": "1065514947"
    }, 
    {
      "name": "Alison Lee", 
      "id": "1065870484"
    }, 
    {
      "name": "Erik Su", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "year": {
            "id": "115222815248992", 
            "name": "2012"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "13917075214", 
            "name": "UC Davis"
          }, 
          "concentration": [
            {
              "id": "109353535758331", 
              "name": "Biomedical Engineering"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "1067014918"
    }, 
    {
      "name": "Eric Lee", 
      "education": [
        {
          "school": {
            "id": "108034402563741", 
            "name": "Cupertino High"
          }, 
          "year": {
            "id": "115222815248992", 
            "name": "2012"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "104009006303595", 
            "name": "Rice University"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "type": "College"
        }
      ], 
      "id": "1067653896"
    }, 
    {
      "name": "Avery Kruger", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "year": {
            "id": "118118634930920", 
            "name": "2012"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "13917075214", 
            "name": "UC Davis"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "type": "College"
        }
      ], 
      "id": "1068126194"
    }, 
    {
      "name": "Will Booth", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "107658532597137", 
            "name": "California Polytechnic State University"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "type": "College"
        }
      ], 
      "id": "1070101772"
    }, 
    {
      "name": "Chihiro Tamefusa", 
      "education": [
        {
          "school": {
            "id": "106523189385484", 
            "name": "Shibuya Makuhari High School"
          }, 
          "type": "High School", 
          "classes": [
            {
              "id": "255011587927886", 
              "name": "27th Returnees", 
              "with": [
                {
                  "id": "100000774597455", 
                  "name": "Daniel Wang"
                }
              ], 
              "from": {
                "id": "100000774597455", 
                "name": "Daniel Wang"
              }
            }
          ]
        }, 
        {
          "school": {
            "id": "114275061922953", 
            "name": ""
          }, 
          "type": "High School", 
          "classes": [
            {
              "id": "166323320156410", 
              "name": "27", 
              "with": [
                {
                  "id": "100000774597455", 
                  "name": "Daniel Wang"
                }
              ], 
              "from": {
                "id": "100000774597455", 
                "name": "Daniel Wang"
              }
            }, 
            {
              "id": "106243676123197", 
              "name": "", 
              "with": [
                {
                  "id": "100001780331815", 
                  "name": "Keisuke Saegusa"
                }
              ], 
              "from": {
                "id": "100001780331815", 
                "name": "Keisuke Saegusa"
              }
            }, 
            {
              "id": "195974100415280", 
              "name": "3I", 
              "with": [
                {
                  "id": "100002612346193", 
                  "name": "Yoshiaki  Ohkawara"
                }, 
                {
                  "id": "1572528411", 
                  "name": "Chizuru Kobayashi"
                }, 
                {
                  "id": "1291151882", 
                  "name": "Shigeo Iizuka"
                }, 
                {
                  "id": "100001321866223", 
                  "name": "Mei Hirata"
                }, 
                {
                  "id": "100000451992580", 
                  "name": "Minami Fukuyama"
                }, 
                {
                  "id": "100003156006350", 
                  "name": "Reimi  Morishita"
                }, 
                {
                  "id": "1185880664", 
                  "name": "Rena Sasahara"
                }, 
                {
                  "id": "1097317592", 
                  "name": "Ellie Kubota"
                }, 
                {
                  "id": "598047320", 
                  "name": "Yuki Numata"
                }
              ]
            }, 
            {
              "id": "198839343460772", 
              "name": "2B", 
              "with": [
                {
                  "id": "1291151882", 
                  "name": "Shigeo Iizuka"
                }, 
                {
                  "id": "1185880664", 
                  "name": "Rena Sasahara"
                }, 
                {
                  "id": "1097317592", 
                  "name": "Ellie Kubota"
                }
              ]
            }, 
            {
              "id": "164537173597311", 
              "name": "1b", 
              "with": [
                {
                  "id": "100001780331815", 
                  "name": "Keisuke Saegusa"
                }, 
                {
                  "id": "100001363754053", 
                  "name": "Reiko Ishida"
                }, 
                {
                  "id": "1460631599", 
                  "name": "Maho Takasawa"
                }, 
                {
                  "id": "1097317592", 
                  "name": "Ellie Kubota"
                }
              ]
            }, 
            {
              "id": "101212390001228", 
              "name": "3/1", 
              "with": [
                {
                  "id": "1185880664", 
                  "name": "Rena Sasahara"
                }, 
                {
                  "id": "1097317592", 
                  "name": "Ellie Kubota"
                }
              ]
            }, 
            {
              "id": "199183306758611", 
              "name": "2/3", 
              "with": [
                {
                  "id": "1358063498", 
                  "name": "Amy Nagamine"
                }, 
                {
                  "id": "100001363754053", 
                  "name": "Reiko Ishida"
                }, 
                {
                  "id": "1711352159", 
                  "name": "Miku Iwasaki"
                }, 
                {
                  "id": "1185880664", 
                  "name": "Rena Sasahara"
                }, 
                {
                  "id": "661300280", 
                  "name": "Taimu Hirayama"
                }
              ]
            }, 
            {
              "id": "181481578554051", 
              "name": "1/7", 
              "with": [
                {
                  "id": "100003252291605", 
                  "name": "Akane Katayama"
                }, 
                {
                  "id": "1456794325", 
                  "name": "Ayaka Horikiri"
                }, 
                {
                  "id": "1607472675", 
                  "name": "Yuki Hasuda"
                }, 
                {
                  "id": "1097317592", 
                  "name": "Ellie Kubota"
                }
              ]
            }
          ]
        }, 
        {
          "school": {
            "id": "136041456595139", 
            "name": "Shibumaku"
          }, 
          "year": {
            "id": "118118634930920", 
            "name": "2012"
          }, 
          "type": "High School", 
          "classes": [
            {
              "id": "181481578554051", 
              "name": "1/7", 
              "with": [
                {
                  "id": "1607472675", 
                  "name": "Yuki Hasuda"
                }
              ], 
              "from": {
                "id": "1607472675", 
                "name": "Yuki Hasuda"
              }
            }, 
            {
              "id": "328331277218725", 
              "name": "Returnee English", 
              "with": [
                {
                  "id": "1607472675", 
                  "name": "Yuki Hasuda"
                }
              ], 
              "from": {
                "id": "1607472675", 
                "name": "Yuki Hasuda"
              }
            }
          ]
        }, 
        {
          "school": {
            "id": "108141012547474", 
            "name": "Darien High School"
          }, 
          "year": {
            "id": "118118634930920", 
            "name": "2012"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "25827817664", 
            "name": "Pomona College"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "type": "College"
        }
      ], 
      "id": "1070388589"
    }, 
    {
      "name": "Angie Bi", 
      "education": [
        {
          "school": {
            "id": "106168309414731", 
            "name": "Rancho Cucamonga High School"
          }, 
          "year": {
            "id": "118118634930920", 
            "name": "2012"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "103756122996046", 
            "name": "Pomona College"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "type": "College", 
          "classes": [
            {
              "id": "170481426331222", 
              "name": "2016"
            }
          ]
        }
      ], 
      "id": "1075478991"
    }, 
    {
      "name": "Karen Rodya Ouyang", 
      "education": [
        {
          "school": {
            "id": "109748892385588", 
            "name": "Lynbrook High School"
          }, 
          "year": {
            "id": "120960561375312", 
            "name": "2013"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "18058830773", 
            "name": "Princeton University"
          }, 
          "type": "College"
        }
      ], 
      "id": "1075832344"
    }, 
    {
      "name": "Priya Vijaykumar", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "245640871929", 
            "name": "The University of Texas at Austin"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "concentration": [
            {
              "id": "109314462420288", 
              "name": "Biology"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "1077001780"
    }, 
    {
      "name": "Darren Hau", 
      "education": [
        {
          "school": {
            "id": "109828372368206", 
            "name": "Los Gatos High School"
          }, 
          "year": {
            "id": "201638419856163", 
            "name": "2011"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "6192688417", 
            "name": "Stanford University"
          }, 
          "year": {
            "id": "105576766163075", 
            "name": "2015"
          }, 
          "type": "College"
        }
      ], 
      "id": "1079926125"
    }, 
    {
      "name": "Belicia Ding", 
      "education": [
        {
          "school": {
            "id": "394406330660457", 
            "name": ""
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "108271019195309", 
            "name": "Gunn High School"
          }, 
          "year": {
            "id": "144044875610606", 
            "name": "2011"
          }, 
          "type": "High School", 
          "classes": [
            {
              "id": "125330810872293", 
              "name": "Yearbook", 
              "with": [
                {
                  "id": "672962145", 
                  "name": "Kathrina Casapao Onate"
                }
              ], 
              "from": {
                "id": "672962145", 
                "name": "Kathrina Casapao Onate"
              }
            }
          ]
        }, 
        {
          "school": {
            "id": "104009006303595", 
            "name": "Rice University"
          }, 
          "year": {
            "id": "105576766163075", 
            "name": "2015"
          }, 
          "type": "College"
        }
      ], 
      "id": "1083735326"
    }, 
    {
      "name": "Leona Zhu", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "28972094743", 
            "name": "University of the Pacific"
          }, 
          "type": "College"
        }
      ], 
      "id": "1089344359"
    }, 
    {
      "name": "Ariel Lee", 
      "education": [
        {
          "school": {
            "id": "110319228989015", 
            "name": "Hopkins Jr. High"
          }, 
          "year": {
            "id": "141778012509913", 
            "name": "2008"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "year": {
            "id": "120960561375312", 
            "name": "2013"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "45408742662", 
            "name": "San Jose State University"
          }, 
          "year": {
            "id": "532490046771314", 
            "name": "2017"
          }, 
          "concentration": [
            {
              "id": "109803049037749", 
              "name": "Graphic Design"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "1089857220"
    }, 
    {
      "name": "Terence Hu", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "year": {
            "id": "143641425651920", 
            "name": "2014"
          }, 
          "type": "High School"
        }
      ], 
      "id": "1089878355"
    }, 
    {
      "name": "Nicholas Krulee", 
      "education": [
        {
          "school": {
            "id": "112040008807941", 
            "name": "Abraham Lincoln High School"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "103776429661094", 
            "name": "Cornish College of the Arts"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "type": "College"
        }
      ], 
      "id": "1093102498"
    }, 
    {
      "name": "Jasmine Lau", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School", 
          "classes": [
            {
              "id": "188918704461958", 
              "name": "2012"
            }
          ]
        }, 
        {
          "school": {
            "id": "107727705916498", 
            "name": "University of California, Riverside"
          }, 
          "type": "College", 
          "classes": [
            {
              "id": "170481426331222", 
              "name": "2016"
            }
          ]
        }
      ], 
      "id": "1099774674"
    }, 
    {
      "name": "Andy Lai", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "year": {
            "id": "143641425651920", 
            "name": "2014"
          }, 
          "type": "High School"
        }
      ], 
      "id": "1108537536"
    }, 
    {
      "name": "Gerilyn Olsen", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "108331145854226", 
            "name": "Harker School"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "112795212068138", 
            "name": "Washington University in St. Louis"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "type": "College"
        }
      ], 
      "id": "1109033794"
    }, 
    {
      "name": "Jennifer Sekar", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "21489041474", 
            "name": "Duke University"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "type": "College"
        }
      ], 
      "id": "1126501994"
    }, 
    {
      "name": "Aik Meng Tan", 
      "education": [
        {
          "school": {
            "id": "106253592746373", 
            "name": "Dunman Secondary School"
          }, 
          "year": {
            "id": "130747936967273", 
            "name": "1983"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "114917321853004", 
            "name": "Singapore Polytechnic"
          }, 
          "year": {
            "id": "136666673036069", 
            "name": "1987"
          }, 
          "type": "College"
        }
      ], 
      "id": "1128440392"
    }, 
    {
      "name": "Jay Shah", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "108296752532618", 
            "name": "Georgia Institute of Technology College of Engineering"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "concentration": [
            {
              "id": "109353535758331", 
              "name": "Biomedical Engineering"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "1132397556"
    }, 
    {
      "name": "Christy Chen", 
      "education": [
        {
          "school": {
            "id": "109748892385588", 
            "name": "Lynbrook High School"
          }, 
          "type": "High School", 
          "classes": [
            {
              "id": "188918704461958", 
              "name": "2012"
            }
          ]
        }, 
        {
          "school": {
            "id": "25855743604", 
            "name": "Indiana University Jacobs School of Music"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "concentration": [
            {
              "id": "128845670519714", 
              "name": "Violin Performance"
            }
          ], 
          "type": "College", 
          "classes": [
            {
              "id": "252311344788965", 
              "name": "Indiana University - Class of 2016"
            }
          ]
        }
      ], 
      "id": "1133096376"
    }, 
    {
      "name": "Albert Chang", 
      "education": [
        {
          "school": {
            "id": "112310598785658", 
            "name": "University High School (Fresno)"
          }, 
          "year": {
            "id": "142963519060927", 
            "name": "2010"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "103756122996046", 
            "name": "Pomona College"
          }, 
          "year": {
            "id": "143641425651920", 
            "name": "2014"
          }, 
          "type": "College"
        }
      ], 
      "id": "1135981053"
    }, 
    {
      "name": "Tien Le", 
      "education": [
        {
          "school": {
            "id": "201983926531012", 
            "name": "Thomas Jefferson"
          }, 
          "year": {
            "id": "115222815248992", 
            "name": "2012"
          }, 
          "type": "High School", 
          "classes": [
            {
              "id": "55200621163", 
              "name": "2012"
            }
          ]
        }, 
        {
          "school": {
            "id": "25827817664", 
            "name": "Pomona College"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "type": "College"
        }
      ], 
      "id": "1148034681"
    }, 
    {
      "name": "Arthur Jeng", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "year": {
            "id": "144044875610606", 
            "name": "2011"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "114642418551886", 
            "name": "UC Berkeley"
          }, 
          "year": {
            "id": "105576766163075", 
            "name": "2015"
          }, 
          "type": "College"
        }
      ], 
      "id": "1149002797"
    }, 
    {
      "name": "Catherine Shi", 
      "id": "1158469878"
    }, 
    {
      "name": "Sara Shi", 
      "education": [
        {
          "school": {
            "id": "106396909396987", 
            "name": "Nicolet High"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "103756122996046", 
            "name": "Pomona College"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "concentration": [
            {
              "id": "106104499421077", 
              "name": "Molecular Biology"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "1162106068"
    }, 
    {
      "name": "Kevin Lee", 
      "education": [
        {
          "school": {
            "id": "112734332072619", 
            "name": "Palo Alto High School"
          }, 
          "year": {
            "id": "115222815248992", 
            "name": "2012"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "10111634660", 
            "name": "UC Berkeley"
          }, 
          "type": "College"
        }
      ], 
      "id": "1162614544"
    }, 
    {
      "name": "Joshua Hua Shao", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "year": {
            "id": "138879996141011", 
            "name": "2013"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "112545315425325", 
            "name": "Santa Clara University"
          }, 
          "concentration": [
            {
              "id": "112092048806093", 
              "name": "Business Marketing"
            }, 
            {
              "id": "104045469631213", 
              "name": "Political Science"
            }, 
            {
              "id": "193207117373238", 
              "name": "Studio Art/Graphic Design"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "1166072596"
    }, 
    {
      "name": "Catherine Li", 
      "education": [
        {
          "school": {
            "id": "111964282150016", 
            "name": "Los Altos High School"
          }, 
          "type": "High School"
        }
      ], 
      "id": "1167502279"
    }, 
    {
      "name": "Cindy Lewis", 
      "education": [
        {
          "school": {
            "id": "112525512096586", 
            "name": "Chatsworth High School"
          }, 
          "year": {
            "id": "105127589543050", 
            "name": "1976"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "24743274366", 
            "name": "California Polytechnic State University (Cal Poly)"
          }, 
          "year": {
            "id": "149402035069887", 
            "name": "1981"
          }, 
          "concentration": [
            {
              "id": "106113266087535", 
              "name": "Architectural Engineering"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "1171772410"
    }, 
    {
      "name": "Minmin Fu", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "year": {
            "id": "143641425651920", 
            "name": "2014"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "112199395458691", 
            "name": "University of California, Davis"
          }, 
          "concentration": [
            {
              "id": "103966102974293", 
              "name": "Mathematics"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "1172972779"
    }, 
    {
      "name": "Louis Leung", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }
      ], 
      "id": "1177612450"
    }, 
    {
      "name": "Karen Alejandra Herrera", 
      "education": [
        {
          "school": {
            "id": "111859785500054", 
            "name": "La Puente High"
          }, 
          "type": "High School", 
          "with": [
            {
              "id": "100001595480221", 
              "name": "Stephanie Sosa"
            }
          ]
        }, 
        {
          "school": {
            "id": "103756122996046", 
            "name": "Pomona College"
          }, 
          "year": {
            "id": "105576766163075", 
            "name": "2015"
          }, 
          "concentration": [
            {
              "id": "183304948432132", 
              "name": "Stuff."
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "1178612715"
    }, 
    {
      "name": "Kaavya Valiveti", 
      "education": [
        {
          "school": {
            "id": "103991312969759", 
            "name": "Mission San Jose High School"
          }, 
          "year": {
            "id": "115222815248992", 
            "name": "2012"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "108639099168058", 
            "name": "University of California, Berkeley"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "type": "College"
        }
      ], 
      "id": "1178961866"
    }, 
    {
      "name": "Aaron Yuan", 
      "id": "1179506953"
    }, 
    {
      "name": "Alice Park", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "10111634660", 
            "name": "UC Berkeley"
          }, 
          "type": "College"
        }
      ], 
      "id": "1182357577"
    }, 
    {
      "name": "Bernard Nguyen", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "year": {
            "id": "138879996141011", 
            "name": "2013"
          }, 
          "type": "High School"
        }
      ], 
      "id": "1185112825"
    }, 
    {
      "name": "Jason Chen", 
      "education": [
        {
          "school": {
            "id": "108034402563741", 
            "name": "Cupertino High"
          }, 
          "year": {
            "id": "138879996141011", 
            "name": "2013"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "7133766387", 
            "name": "Carnegie Mellon University"
          }, 
          "year": {
            "id": "532490046771314", 
            "name": "2017"
          }, 
          "concentration": [
            {
              "id": "108406612523064", 
              "name": "Information Systems"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "1189980097"
    }, 
    {
      "name": "Ryan Tang", 
      "education": [
        {
          "school": {
            "id": "103991312969759", 
            "name": "Mission San Jose High School"
          }, 
          "year": {
            "id": "115222815248992", 
            "name": "2012"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "108877405802697", 
            "name": "University of Chicago"
          }, 
          "type": "College"
        }
      ], 
      "id": "1190743913"
    }, 
    {
      "name": "Kavita Jain", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "108047109223278", 
            "name": "University of California, San Diego"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "type": "College"
        }
      ], 
      "id": "1197130236"
    }, 
    {
      "name": "Ada Kwong", 
      "education": [
        {
          "school": {
            "id": "103991312969759", 
            "name": "Mission San Jose High School"
          }, 
          "year": {
            "id": "120960561375312", 
            "name": "2013"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "112268392119059", 
            "name": "Sacramento City College"
          }, 
          "concentration": [
            {
              "id": "109314462420288", 
              "name": "Biology"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "1198560536"
    }, 
    {
      "name": "Helen Brahms Wu", 
      "education": [
        {
          "school": {
            "id": "108331145854226", 
            "name": "Harker School"
          }, 
          "year": {
            "id": "105576766163075", 
            "name": "2015"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "108546012510012", 
            "name": "The Harker School"
          }, 
          "type": "High School", 
          "classes": [
            {
              "id": "112906985452359", 
              "name": "2015 :)", 
              "with": [
                {
                  "id": "1277383078", 
                  "name": "Jeffrey Shoe"
                }, 
                {
                  "id": "1041040075", 
                  "name": "Andrew J Zhang"
                }
              ], 
              "from": {
                "id": "1041040075", 
                "name": "Andrew J Zhang"
              }
            }
          ]
        }
      ], 
      "id": "1199381996"
    }, 
    {
      "name": "Kaori Isobe", 
      "id": "1201104326"
    }, 
    {
      "name": "Sean Xin", 
      "education": [
        {
          "school": {
            "id": "103053219734496", 
            "name": "Hwa Chong Institution"
          }, 
          "year": {
            "id": "142963519060927", 
            "name": "2010"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "103098179730314", 
            "name": "Hwa Chong Junior College"
          }, 
          "year": {
            "id": "115222815248992", 
            "name": "2012"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "103756122996046", 
            "name": "Pomona College"
          }, 
          "type": "College"
        }
      ], 
      "id": "1202364224"
    }, 
    {
      "name": "Henry Allison", 
      "education": [
        {
          "school": {
            "id": "112235968793130", 
            "name": "Homestead High School"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "108582099172607", 
            "name": "Oberlin Conservatory of Music"
          }, 
          "year": {
            "id": "105576766163075", 
            "name": "2015"
          }, 
          "concentration": [
            {
              "id": "128845670519714", 
              "name": "Violin Performance"
            }
          ], 
          "type": "College"
        }, 
        {
          "school": {
            "id": "110304992323560", 
            "name": "Oberlin College Conservatory of Music"
          }, 
          "type": "Graduate School"
        }
      ], 
      "id": "1206505514"
    }, 
    {
      "name": "Calvin Leung", 
      "education": [
        {
          "school": {
            "id": "144039478952193", 
            "name": "Mission San Jose High School"
          }, 
          "year": {
            "id": "120960561375312", 
            "name": "2013"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "280782445277463", 
            "name": "UC Davis Cosmos"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "328427100886", 
            "name": "INSPIRE-Online Learning Community (Official NASA Project)"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "124056590943812", 
            "name": "Harvey Mudd College"
          }, 
          "year": {
            "id": "532490046771314", 
            "name": "2017"
          }, 
          "type": "College", 
          "classes": [
            {
              "id": "179039122137632", 
              "name": "Class of 2017"
            }
          ]
        }
      ], 
      "id": "1210920966"
    }, 
    {
      "name": "Kunal Shah", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "134972803193847", 
            "name": "University of Southern California"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "type": "College"
        }
      ], 
      "id": "1211942908"
    }, 
    {
      "name": "Darryl Vo", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "14853016605", 
            "name": "Cal Poly SLO"
          }, 
          "type": "College"
        }
      ], 
      "id": "1213352148"
    }, 
    {
      "name": "Stacey Abrams", 
      "id": "1216776724"
    }, 
    {
      "name": "Aaron Ching", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "106384006064200", 
            "name": "Mission San Jose High"
          }, 
          "year": {
            "id": "143641425651920", 
            "name": "2014"
          }, 
          "type": "College"
        }
      ], 
      "id": "1224267394"
    }, 
    {
      "name": "Lauren Taylor", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "year": {
            "id": "118118634930920", 
            "name": "2012"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "134972803193847", 
            "name": "University of Southern California"
          }, 
          "concentration": [
            {
              "id": "108535589178153", 
              "name": "Biological Sciences"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "1227481734"
    }, 
    {
      "name": "Kevin Sheu", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "11360325957", 
            "name": "UCLA"
          }, 
          "type": "College"
        }
      ], 
      "id": "1231963921"
    }, 
    {
      "name": "Eileen Wong", 
      "id": "1234146823"
    }, 
    {
      "name": "Stephen Eng", 
      "id": "1241113913"
    }, 
    {
      "name": "Dora Wang", 
      "education": [
        {
          "school": {
            "id": "112729635408723", 
            "name": "Prospect High School (California)"
          }, 
          "type": "High School"
        }
      ], 
      "id": "1244681758"
    }, 
    {
      "name": "Angela Zhu", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "112520115426955", 
            "name": "University of Pennsylvania"
          }, 
          "type": "College", 
          "classes": [
            {
              "id": "243728472331028", 
              "name": "Chemistry"
            }
          ]
        }
      ], 
      "id": "1250935950"
    }, 
    {
      "name": "Kristen Silva-Robles", 
      "education": [
        {
          "school": {
            "id": "110360665650668", 
            "name": "Harbor High"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "103756122996046", 
            "name": "Pomona College"
          }, 
          "type": "College"
        }
      ], 
      "id": "1252432826"
    }, 
    {
      "name": "Julie Saigusa", 
      "id": "1252497152"
    }, 
    {
      "name": "Byron Chou", 
      "education": [
        {
          "school": {
            "id": "108018522552037", 
            "name": "Leland High School"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "28972094743", 
            "name": "University of the Pacific"
          }, 
          "type": "College"
        }
      ], 
      "id": "1254191112"
    }, 
    {
      "name": "Khanh L. Nguyen", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School", 
          "classes": [
            {
              "id": "196885043671079", 
              "name": "2012-2013"
            }
          ]
        }, 
        {
          "school": {
            "id": "31914238787", 
            "name": "Eastman School of Music"
          }, 
          "year": {
            "id": "532490046771314", 
            "name": "2017"
          }, 
          "type": "College", 
          "classes": [
            {
              "id": "172633739449210", 
              "name": "Classical Saxophone Performance"
            }, 
            {
              "id": "383168308365598", 
              "name": "Music Education"
            }
          ]
        }
      ], 
      "id": "1257923804"
    }, 
    {
      "name": "David Guo", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "11360325957", 
            "name": "UCLA"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "type": "College", 
          "classes": [
            {
              "id": "182459431796117", 
              "name": "Class of 2016"
            }
          ]
        }
      ], 
      "id": "1258693903"
    }, 
    {
      "name": "Eric ChewcolateDonat Xie", 
      "education": [
        {
          "school": {
            "id": "109748892385588", 
            "name": "Lynbrook High School"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "10111634660", 
            "name": "UC Berkeley"
          }, 
          "type": "College"
        }
      ], 
      "id": "1261280092"
    }, 
    {
      "name": "Alex Chong", 
      "education": [
        {
          "school": {
            "id": "105594282808531", 
            "name": "Davis Senior High School"
          }, 
          "year": {
            "id": "118118634930920", 
            "name": "2012"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "112660892079422", 
            "name": "Pitzer College"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "type": "College"
        }
      ], 
      "id": "1264533747"
    }, 
    {
      "name": "David Chung", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "146939692033407", 
            "name": "University of California Santa Barbara"
          }, 
          "type": "College"
        }
      ], 
      "id": "1266035268"
    }, 
    {
      "name": "Niuniu Teo", 
      "education": [
        {
          "school": {
            "id": "116074151736183", 
            "name": "Pinewood"
          }, 
          "year": {
            "id": "118118634930920", 
            "name": "2012"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "6192688417", 
            "name": "Stanford University"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "type": "College"
        }
      ], 
      "id": "1266702107"
    }, 
    {
      "name": "Binjih Lin", 
      "education": [
        {
          "school": {
            "id": "103991312969759", 
            "name": "Mission San Jose High School"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "year": {
            "id": "118118634930920", 
            "name": "2012"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "105517352815443", 
            "name": "California Institute of Technology"
          }, 
          "type": "College"
        }, 
        {
          "school": {
            "id": "110116389018278", 
            "name": "Caltech"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "concentration": [
            {
              "id": "109532545739630", 
              "name": "Engineering"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "1267073379"
    }, 
    {
      "name": "Selina Her", 
      "id": "1267943956"
    }, 
    {
      "name": "Hong Suh", 
      "education": [
        {
          "school": {
            "id": "108034402563741", 
            "name": "Cupertino High"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "25827817664", 
            "name": "Pomona College"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "concentration": [
            {
              "id": "107756862591509", 
              "name": "Math"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "1282798041"
    }, 
    {
      "name": "Leland Bernstein", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "year": {
            "id": "118118634930920", 
            "name": "2012"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "112520115426955", 
            "name": "University of Pennsylvania"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "type": "College"
        }
      ], 
      "id": "1288357037"
    }, 
    {
      "name": "Michael Tan", 
      "id": "1294770478"
    }, 
    {
      "name": "Laura Conn", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "6096033309", 
            "name": "The University of Arizona"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "type": "College"
        }
      ], 
      "id": "1299133129"
    }, 
    {
      "name": "Jennifer J. Kim", 
      "id": "1302478236"
    }, 
    {
      "name": "Dennis Chiang", 
      "education": [
        {
          "school": {
            "id": "102079169833347", 
            "name": "Westview High School"
          }, 
          "year": {
            "id": "115222815248992", 
            "name": "2012"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "108047109223278", 
            "name": "University of California, San Diego"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "concentration": [
            {
              "id": "106166156082069", 
              "name": "Electrical Engineering"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "1310387197"
    }, 
    {
      "name": "Prasanna Rajan", 
      "id": "1313511047"
    }, 
    {
      "name": "Phoebe Wu", 
      "education": [
        {
          "school": {
            "id": "78677447695", 
            "name": "University of Michigan School of Music, Theatre & Dance"
          }, 
          "year": {
            "id": "532490046771314", 
            "name": "2017"
          }, 
          "type": "College"
        }, 
        {
          "school": {
            "id": "130447023765082", 
            "name": "Los Gatos High"
          }, 
          "year": {
            "id": "138879996141011", 
            "name": "2013"
          }, 
          "type": "College"
        }
      ], 
      "id": "1318170968"
    }, 
    {
      "name": "Monique Nguyen", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School", 
          "classes": [
            {
              "id": "161878910530139", 
              "name": "Class of 2012"
            }
          ]
        }
      ], 
      "id": "1318604198"
    }, 
    {
      "name": "Mehul Goyal", 
      "id": "1318715846"
    }, 
    {
      "name": "Andy Cheon", 
      "education": [
        {
          "school": {
            "id": "114659898545497", 
            "name": "Monta Vista High"
          }, 
          "year": {
            "id": "144044875610606", 
            "name": "2011"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "10111634660", 
            "name": "UC Berkeley"
          }, 
          "year": {
            "id": "105576766163075", 
            "name": "2015"
          }, 
          "type": "College"
        }
      ], 
      "id": "1319056901"
    }, 
    {
      "name": "Nate Kan", 
      "education": [
        {
          "school": {
            "id": "142582035773065", 
            "name": "Mission San Jose Elementary School"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "115044455174147", 
            "name": "Hopkins Junior High"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "103991312969759", 
            "name": "Mission San Jose High School"
          }, 
          "year": {
            "id": "115222815248992", 
            "name": "2012"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "113079308707134", 
            "name": "Pacific Union College"
          }, 
          "concentration": [
            {
              "id": "163541940364276", 
              "name": "Pre-Physical Therapy"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "1324861660"
    },
    {
      "name": "Aloke Desai", 
      "education": [
        {
          "school": {
            "id": "110497035645916", 
            "name": "Indian Hill"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "25827817664", 
            "name": "Pomona College"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "type": "College"
        }
      ], 
      "id": "1329020679"
    }, 
    {
      "name": "Jee Young Kim", 
      "education": [
        {
          "school": {
            "id": "109642382395535", 
            "name": "Monta Vista High School"
          }, 
          "year": {
            "id": "143641425651920", 
            "name": "2014"
          }, 
          "type": "High School"
        }
      ], 
      "id": "1330373302"
    }, 
    {
      "name": "Kevin Hsu", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "104328202999303", 
            "name": "UC San Diego"
          }, 
          "type": "College"
        }, 
        {
          "school": {
            "id": "108047109223278", 
            "name": "University of California, San Diego"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "concentration": [
            {
              "id": "106166156082069", 
              "name": "Electrical Engineering"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "1335971898"
    }, 
    {
      "name": "Ashley Wu", 
      "education": [
        {
          "school": {
            "id": "109642382395535", 
            "name": "Monta Vista High School"
          }, 
          "year": {
            "id": "118118634930920", 
            "name": "2012"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "228401243342", 
            "name": "Northwestern University"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "concentration": [
            {
              "id": "107512149278840", 
              "name": "Journalism"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "1345244291"
    }, 
    {
      "name": "I-Ling Chiang", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "126533127390327", 
            "name": "Massachusetts Institute of Technology (MIT)"
          }, 
          "type": "College"
        }
      ], 
      "id": "1345802140"
    }, 
    {
      "name": "Anmol Gill", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "107888572565045", 
            "name": "University of California, Santa Barbara"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "concentration": [
            {
              "id": "100664446680556", 
              "name": "Biopsychology"
            }
          ], 
          "type": "College", 
          "classes": [
            {
              "id": "182459431796117", 
              "name": "Class of 2016"
            }
          ]
        }
      ], 
      "id": "1346693237"
    }, 
    {
      "name": "Sonia Liou", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "year": {
            "id": "118118634930920", 
            "name": "2012"
          }, 
          "type": "High School"
        }
      ], 
      "id": "1347131156"
    }, 
    {
      "name": "Vincent Nguyen", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "7093532993", 
            "name": "Ohlone College"
          }, 
          "type": "College"
        }
      ], 
      "id": "1347669638"
    }, 
    {
      "name": "Chanud Yasanayake", 
      "id": "1348329887"
    }, 
    {
      "name": "Jane Oe", 
      "id": "1349577328"
    }, 
    {
      "name": "Hye Young Sarah Choi", 
      "education": [
        {
          "school": {
            "id": "105572882808621", 
            "name": "Cupertino High School"
          }, 
          "year": {
            "id": "293650690709608", 
            "name": "2012"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "34410694953", 
            "name": "De Anza College"
          }, 
          "type": "College"
        }
      ], 
      "id": "1352821178"
    }, 
    {
      "name": "Grace Wu", 
      "education": [
        {
          "school": {
            "id": "351573841586647", 
            "name": "Mission San Jose High School"
          }, 
          "year": {
            "id": "143641425651920", 
            "name": "2014"
          }, 
          "type": "High School"
        }
      ], 
      "id": "1354785077"
    }, 
    {
      "name": "Davy Lu", 
      "education": [
        {
          "school": {
            "id": "116421478379614", 
            "name": "DVHS"
          }, 
          "year": {
            "id": "118118634930920", 
            "name": "2012"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "108231752535298", 
            "name": "Dougherty Valley High School"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "6192688417", 
            "name": "Stanford University"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "concentration": [
            {
              "id": "115266318488264", 
              "name": "Materials Science and Engineering"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "1355364802"
    }, 
    {
      "name": "Sam Du", 
      "education": [
        {
          "school": {
            "id": "105998799431030", 
            "name": "Newport High School"
          }, 
          "year": {
            "id": "118118634930920", 
            "name": "2012"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "25827817664", 
            "name": "Pomona College"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "type": "College"
        }
      ], 
      "id": "1361761096"
    }, 
    {
      "name": "Kevin Chang'", 
      "education": [
        {
          "school": {
            "id": "109642382395535", 
            "name": "Monta Vista High School"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "10111634660", 
            "name": "UC Berkeley"
          }, 
          "type": "College"
        }
      ], 
      "id": "1370270987"
    }, 
    {
      "name": "Gabriel Bronshteyn", 
      "education": [
        {
          "school": {
            "id": "104008059637078", 
            "name": "Monte Vista High School"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "25827817664", 
            "name": "Pomona College"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "concentration": [
            {
              "id": "179398022102115", 
              "name": "Economics and Computer Science"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "1370802012"
    }, 
    {
      "name": "Taemin Ahn", 
      "education": [
        {
          "school": {
            "id": "108212025867060", 
            "name": "Bellarmine College Preparatory"
          }, 
          "year": {
            "id": "138879996141011", 
            "name": "2013"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "108002152557044", 
            "name": "Georgetown University"
          }, 
          "type": "College"
        }
      ], 
      "id": "1373777151"
    }, 
    {
      "name": "Sonya Huang", 
      "education": [
        {
          "school": {
            "id": "108331145854226", 
            "name": "Harker School"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "18058830773", 
            "name": "Princeton University"
          }, 
          "year": {
            "id": "143641425651920", 
            "name": "2014"
          }, 
          "concentration": [
            {
              "id": "108180979203954", 
              "name": "Economics"
            }, 
            {
              "id": "104076956295773", 
              "name": "Computer Science"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "1375435238"
    }, 
    {
      "name": "Sumedh Bhattacharya", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "10111634660", 
            "name": "UC Berkeley"
          }, 
          "year": {
            "id": "532490046771314", 
            "name": "2017"
          }, 
          "concentration": [
            {
              "id": "105573196144184", 
              "name": "Electrical Engineering and Computer Science"
            }
          ], 
          "type": "College"
        }, 
        {
          "school": {
            "id": "154996014522818", 
            "name": "Carnegie Mellon Pre-College Programs"
          }, 
          "year": {
            "id": "115222815248992", 
            "name": "2012"
          }, 
          "type": "College"
        }
      ], 
      "id": "1376168258"
    }, 
    {
      "name": "Maaz Siddiqui", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }
      ], 
      "id": "1376970743"
    }, 
    {
      "name": "Shaina Brady", 
      "id": "1379190696"
    }, 
    {
      "name": "Kevin Chan", 
      "education": [
        {
          "school": {
            "id": "600165130016242", 
            "name": "Mission San Jose Hgh"
          }, 
          "year": {
            "id": "136328419721520", 
            "name": "2009"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "103991312969759", 
            "name": "Mission San Jose High School"
          }, 
          "type": "College"
        }
      ], 
      "id": "1381037999"
    }, 
    {
      "name": "Parth Patel", 
      "education": [
        {
          "school": {
            "id": "104017019634029", 
            "name": "South Forsyth High School"
          }, 
          "year": {
            "id": "144044875610606", 
            "name": "2011"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "103756122996046", 
            "name": "Pomona College"
          }, 
          "year": {
            "id": "105576766163075", 
            "name": "2015"
          }, 
          "type": "College"
        }
      ], 
      "id": "1381321282"
    }, 
    {
      "name": "Willson Zhang", 
      "education": [
        {
          "school": {
            "id": "112271455455353", 
            "name": "San Jose State University"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "concentration": [
            {
              "id": "103724069666039", 
              "name": "Biochemistry"
            }
          ], 
          "type": "College", 
          "classes": [
            {
              "id": "107311799373277", 
              "name": "Pre-Medicine"
            }
          ]
        }
      ], 
      "id": "1382667584"
    }, 
    {
      "name": "Theodora Martin", 
      "education": [
        {
          "school": {
            "id": "110367572318903", 
            "name": "Del Mar High"
          }, 
          "year": {
            "id": "118118634930920", 
            "name": "2012"
          }, 
          "type": "High School", 
          "with": [
            {
              "id": "100001079163873", 
              "name": "Kevin Kirsch"
            }, 
            {
              "id": "100000009764484", 
              "name": "Christine Pham"
            }, 
            {
              "id": "1578884365", 
              "name": "Carmen Muller"
            }, 
            {
              "id": "1215723366", 
              "name": "Bragatheesh Suresh"
            }
          ]
        }, 
        {
          "school": {
            "id": "10111634660", 
            "name": "UC Berkeley"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "concentration": [
            {
              "id": "106059522759137", 
              "name": "English"
            }, 
            {
              "id": "112936425387489", 
              "name": "Music"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "1384134371"
    }, 
    {
      "name": "Alison Kwok", 
      "id": "1387165122"
    }, 
    {
      "name": "Conrad Tao", 
      "education": [
        {
          "school": {
            "id": "114890818521846", 
            "name": "Juilliard Pre-College"
          }, 
          "year": {
            "id": "201638419856163", 
            "name": "2011"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "102471088936", 
            "name": "Columbia University in the City of New York"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "type": "College"
        }, 
        {
          "school": {
            "id": "114501075233366", 
            "name": "Juilliard"
          }, 
          "type": "College"
        }, 
        {
          "school": {
            "id": "109617515731169", 
            "name": "Aspen Music Festival and School"
          }, 
          "type": "College"
        }
      ], 
      "id": "1388040119"
    }, 
    {
      "name": "Tiffany Chen", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }
      ], 
      "id": "1390818790"
    }, 
    {
      "name": "Amy Zeng", 
      "education": [
        {
          "school": {
            "id": "110098575679764", 
            "name": "Foothill High"
          }, 
          "year": {
            "id": "105576766163075", 
            "name": "2015"
          }, 
          "type": "High School"
        }
      ], 
      "id": "1397748398"
    }, 
    {
      "name": "Keith Lewis", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "112271455455353", 
            "name": "San Jose State University"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "type": "College"
        }
      ], 
      "id": "1399159715"
    }, 
    {
      "name": "Sudharsan Sundara", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "13917075214", 
            "name": "UC Davis"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "type": "College"
        }
      ], 
      "id": "1402564604"
    }, 
    {
      "name": "Marisa Yang", 
      "education": [
        {
          "school": {
            "id": "114659898545497", 
            "name": "Monta Vista High"
          }, 
          "year": {
            "id": "143641425651920", 
            "name": "2014"
          }, 
          "type": "High School"
        }
      ], 
      "id": "1403892402"
    }, 
    {
      "name": "Evelina Chiang", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "15932409357", 
            "name": "Syracuse University"
          }, 
          "type": "College"
        }
      ], 
      "id": "1408119972"
    }, 
    {
      "name": "Rachel Yu", 
      "education": [
        {
          "school": {
            "id": "103991312969759", 
            "name": "Mission San Jose High School"
          }, 
          "year": {
            "id": "120960561375312", 
            "name": "2013"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "54707575539", 
            "name": "UC Santa Barbara"
          }, 
          "year": {
            "id": "532490046771314", 
            "name": "2017"
          }, 
          "type": "College"
        }
      ], 
      "id": "1410231571"
    }, 
    {
      "name": "Seido Karasaki", 
      "education": [
        {
          "school": {
            "id": "108384185849770", 
            "name": "Albany High School"
          }, 
          "year": {
            "id": "118118634930920", 
            "name": "2012"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "106915900963", 
            "name": "Oberlin College"
          }, 
          "year": {
            "id": "185588044800194", 
            "name": "2017"
          }, 
          "concentration": [
            {
              "id": "179178312123764", 
              "name": "Viola"
            }, 
            {
              "id": "104083339627297", 
              "name": "Neuroscience"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "1412186831"
    }, 
    {
      "name": "Tony Zhang", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "year": {
            "id": "118118634930920", 
            "name": "2012"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "13917075214", 
            "name": "UC Davis"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "type": "College"
        }
      ], 
      "id": "1414531829"
    }, 
    {
      "name": "Annie Cheng", 
      "education": [
        {
          "school": {
            "id": "103991312969759", 
            "name": "Mission San Jose High School"
          }, 
          "year": {
            "id": "120960561375312", 
            "name": "2013"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "10111634660", 
            "name": "UC Berkeley"
          }, 
          "year": {
            "id": "532490046771314", 
            "name": "2017"
          }, 
          "type": "College"
        }
      ], 
      "id": "1415852074"
    }, 
    {
      "name": "Stacey Yi", 
      "education": [
        {
          "school": {
            "id": "108058285894979", 
            "name": "Irvington High School"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "104009006303595", 
            "name": "Rice University"
          }, 
          "type": "College", 
          "classes": [
            {
              "id": "182459431796117", 
              "name": "Class of 2016"
            }
          ]
        }
      ], 
      "id": "1419849555"
    }, 
    {
      "name": "Kalvin Luo", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "112545315425325", 
            "name": "Santa Clara University"
          }, 
          "concentration": [
            {
              "id": "198555250156530", 
              "name": "Leavey School of Business"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "1421323826"
    }, 
    {
      "name": "Omar El-Sadany", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "169717243109944", 
            "name": "Carnegie Mellon University Class of 2016"
          }, 
          "type": "College"
        }
      ], 
      "id": "1423627439"
    }, 
    {
      "name": "Audrey Dunne", 
      "education": [
        {
          "school": {
            "id": "103756122996046", 
            "name": "Pomona College"
          }, 
          "year": {
            "id": "138879996141011", 
            "name": "2013"
          }, 
          "type": "College"
        }
      ], 
      "id": "1426106019"
    }, 
    {
      "name": "Tien Lu", 
      "id": "1426664087"
    }, 
    {
      "name": "Vipin Dulam", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "year": {
            "id": "118118634930920", 
            "name": "2012"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "146762395367112", 
            "name": "University of Miami"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "concentration": [
            {
              "id": "104083339627297", 
              "name": "Neuroscience"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "1433257347"
    }, 
    {
      "name": "Janis Chan", 
      "education": [
        {
          "school": {
            "id": "102088699833056", 
            "name": "American High"
          }, 
          "year": {
            "id": "142963519060927", 
            "name": "2010"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "116162241736649", 
            "name": "UC Irvine"
          }, 
          "year": {
            "id": "143641425651920", 
            "name": "2014"
          }, 
          "type": "College"
        }
      ], 
      "id": "1435981944"
    }, 
    {
      "name": "Zackary Shaffer", 
      "education": [
        {
          "school": {
            "id": "103991312969759", 
            "name": "Mission San Jose High School"
          }, 
          "year": {
            "id": "115222815248992", 
            "name": "2012"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "112271455455353", 
            "name": "San Jose State University"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "concentration": [
            {
              "id": "215014605191286", 
              "name": "Aviation Operations"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "1435997978"
    }, 
    {
      "name": "Delia Cannon", 
      "education": [
        {
          "school": {
            "id": "105572882808621", 
            "name": "Cupertino High School"
          }, 
          "year": {
            "id": "115222815248992", 
            "name": "2012"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "105454902822165", 
            "name": "San Diego State University"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "type": "College"
        }
      ], 
      "id": "1436742465"
    }, 
    {
      "name": "Armaan Gill", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }
      ], 
      "id": "1438508383"
    }, 
    {
      "name": "Eric Tang", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }
      ], 
      "id": "1440512670"
    }, 
    {
      "name": "Theodore Peng", 
      "id": "1444440023"
    }, 
    {
      "name": "E.j. Crowley", 
      "education": [
        {
          "school": {
            "id": "108384185849770", 
            "name": "Albany High School"
          }, 
          "type": "High School"
        }
      ], 
      "id": "1449936983"
    }, 
    {
      "name": "Christopher Chan", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "181626185181083", 
            "name": "Sacramento State"
          }, 
          "type": "College"
        }
      ], 
      "id": "1451313287"
    }, 
    {
      "name": "Adiza Veronica Ameh", 
      "education": [
        {
          "school": {
            "id": "105483302819286", 
            "name": "Garfield High School"
          }, 
          "year": {
            "id": "118118634930920", 
            "name": "2012"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "110678318959787", 
            "name": "Claremont Colleges"
          }, 
          "type": "College"
        }, 
        {
          "school": {
            "id": "327495810612400", 
            "name": "Pomona College Class of 2016"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "type": "College"
        }
      ], 
      "id": "1452010249"
    }, 
    {
      "name": "Rebecca Wuu", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School", 
          "classes": [
            {
              "id": "188918704461958", 
              "name": "2012"
            }
          ]
        }, 
        {
          "school": {
            "id": "108340039213516", 
            "name": "Peabody Institute of the Johns Hopkins University"
          }, 
          "year": {
            "id": "185588044800194", 
            "name": "2017"
          }, 
          "concentration": [
            {
              "id": "162188593830010", 
              "name": "Piano Performance"
            }, 
            {
              "id": "187941561236865", 
              "name": "Recording/Audio Engineering"
            }
          ], 
          "type": "College", 
          "classes": [
            {
              "id": "179039122137632", 
              "name": "Class of 2017"
            }
          ]
        }
      ], 
      "id": "1455309120"
    }, 
    {
      "name": "Laura Son", 
      "education": [
        {
          "school": {
            "id": "122150409780", 
            "name": "UC San Diego"
          }, 
          "type": "College"
        }
      ], 
      "id": "1462253996"
    }, 
    {
      "name": "Anatolia Evarkiou-Kaku", 
      "id": "1464524154"
    }, 
    {
      "name": "David Wi", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }
      ], 
      "id": "1468306360"
    }, 
    {
      "name": "Joshua Hsieh", 
      "education": [
        {
          "school": {
            "id": "108244679199268", 
            "name": "Santiago High School"
          }, 
          "year": {
            "id": "118118634930920", 
            "name": "2012"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "112935082050100", 
            "name": "Riverside Community College"
          }, 
          "type": "College"
        }
      ], 
      "id": "1470677740"
    }, 
    {
      "name": "Allen Shih", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "108047109223278", 
            "name": "University of California, San Diego"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "concentration": [
            {
              "id": "104076956295773", 
              "name": "Computer Science"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "1471906540"
    }, 
    {
      "name": "Andy Mueller", 
      "id": "1477352182"
    }, 
    {
      "name": "Sunil Shah", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "186291828074120", 
            "name": "Drexel University"
          }, 
          "type": "College"
        }
      ], 
      "id": "1482267141"
    }, 
    {
      "name": "Natalie Liu", 
      "education": [
        {
          "school": {
            "id": "104154589622349", 
            "name": "Saratoga High School"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "13917075214", 
            "name": "UC Davis"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "type": "College"
        }
      ], 
      "id": "1482646716"
    }, 
    {
      "name": "Calum McCarty", 
      "id": "1485452945"
    }, 
    {
      "name": "Kimberly Ona", 
      "education": [
        {
          "school": {
            "id": "114807388532646", 
            "name": "Governor's School for Agriculture"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "106386229398520", 
            "name": "Centreville High School"
          }, 
          "year": {
            "id": "118118634930920", 
            "name": "2012"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "103756122996046", 
            "name": "Pomona College"
          }, 
          "type": "College"
        }, 
        {
          "school": {
            "id": "25827817664", 
            "name": "Pomona College"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "type": "College", 
          "classes": [
            {
              "id": "182459431796117", 
              "name": "Class of 2016"
            }
          ]
        }
      ], 
      "id": "1486423014"
    }, 
    {
      "name": "Dora Li", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "year": {
            "id": "143641425651920", 
            "name": "2014"
          }, 
          "type": "High School"
        }
      ], 
      "id": "1491254939"
    }, 
    {
      "name": "Jaynelle Gao", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "year": {
            "id": "138879996141011", 
            "name": "2013"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "134972803193847", 
            "name": "University of Southern California"
          }, 
          "type": "College"
        }
      ], 
      "id": "1496290753"
    }, 
    {
      "name": "Charmaine Garzon", 
      "education": [
        {
          "school": {
            "id": "110607258967745", 
            "name": "St. Ignatius College Prep"
          }, 
          "year": {
            "id": "118118634930920", 
            "name": "2012"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "110678318959787", 
            "name": "Claremont Colleges"
          }, 
          "type": "College"
        }, 
        {
          "school": {
            "id": "103756122996046", 
            "name": "Pomona College"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "concentration": [
            {
              "id": "108507619171523", 
              "name": "Psychology"
            }, 
            {
              "id": "312525296370", 
              "name": "Spanish"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "1496791789"
    }, 
    {
      "name": "Brendan Wong", 
      "education": [
        {
          "school": {
            "id": "108231752535298", 
            "name": "Dougherty Valley High School"
          }, 
          "year": {
            "id": "143641425651920", 
            "name": "2014"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }
      ], 
      "id": "1497990312"
    }, 
    {
      "name": "Heather Ha", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }
      ], 
      "id": "1498632407"
    }, 
    {
      "name": "Cecily Celery Lan", 
      "id": "1513637244"
    }, 
    {
      "name": "Shannon Choi", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "13917075214", 
            "name": "UC Davis"
          }, 
          "concentration": [
            {
              "id": "103724069666039", 
              "name": "Biochemistry"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "1515760852"
    }, 
    {
      "name": "Hamilton Trin", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "11360325957", 
            "name": "UCLA"
          }, 
          "type": "College", 
          "classes": [
            {
              "id": "182459431796117", 
              "name": "Class of 2016"
            }
          ]
        }
      ], 
      "id": "1521410143"
    }, 
    {
      "name": "Harley Botak", 
      "id": "1522238674"
    }, 
    {
      "name": "Patrick Yang", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "173767546016882", 
            "name": "UCLA (University of California, LA)"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "concentration": [
            {
              "id": "104011699634001", 
              "name": "Chemical Engineering"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "1522761819"
    }, 
    {
      "name": "Nathan Magalit Suh", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School", 
          "classes": [
            {
              "id": "188918704461958", 
              "name": "2012"
            }
          ]
        }, 
        {
          "school": {
            "id": "13917075214", 
            "name": "UC Davis"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "type": "College", 
          "classes": [
            {
              "id": "182459431796117", 
              "name": "Class of 2016"
            }
          ]
        }
      ], 
      "id": "1525655037"
    }, 
    {
      "name": "Zongning Zhang", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School", 
          "classes": [
            {
              "id": "134982926569619", 
              "name": "Class of 2014!"
            }
          ]
        }
      ], 
      "id": "1533881890"
    }, 
    {
      "name": "Sole Chang", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "109551572397323", 
            "name": "University of Michigan"
          }, 
          "type": "College"
        }
      ], 
      "id": "1534099000"
    }, 
    {
      "name": "Lucy Shen", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "year": {
            "id": "138879996141011", 
            "name": "2013"
          }, 
          "type": "High School", 
          "with": [
            {
              "id": "1230838432", 
              "name": "Bearr Hoffman"
            }
          ]
        }, 
        {
          "school": {
            "id": "416620328391382", 
            "name": "Wellesley College Class of 2017"
          }, 
          "type": "College"
        }
      ], 
      "id": "1535056002"
    }, 
    {
      "name": "Leadz Dorce", 
      "education": [
        {
          "school": {
            "id": "140998521533", 
            "name": "Brown University"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "110512858976802", 
            "name": "International Baccalaureate School"
          }, 
          "year": {
            "id": "293650690709608", 
            "name": "2012"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "104073636296325", 
            "name": "Brown University"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "concentration": [
            {
              "id": "109314462420288", 
              "name": "Biology"
            }, 
            {
              "id": "108433772520758", 
              "name": "Pre Med"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "1536495081"
    }, 
    {
      "name": "Dev Roy", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "13917075214", 
            "name": "UC Davis"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "concentration": [
            {
              "id": "112392142107417", 
              "name": "Biotechnology"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "1537006450"
    }, 
    {
      "name": "Cecilia Yip", 
      "education": [
        {
          "school": {
            "id": "103991312969759", 
            "name": "Mission San Jose High School"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "107604129268675", 
            "name": "Hopkins Junior High School"
          }, 
          "year": {
            "id": "115222815248992", 
            "name": "2012"
          }, 
          "type": "High School", 
          "classes": [
            {
              "id": "188918704461958", 
              "name": "2012"
            }
          ]
        }
      ], 
      "id": "1551428866"
    }, 
    {
      "name": "Jin Peng", 
      "education": [
        {
          "school": {
            "id": "351573841586647", 
            "name": "Mission San Jose High School"
          }, 
          "year": {
            "id": "143641425651920", 
            "name": "2014"
          }, 
          "type": "High School"
        }
      ], 
      "id": "1554695975"
    }, 
    {
      "name": "Gregory An", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }
      ], 
      "id": "1558062907"
    }, 
    {
      "name": "Justin Chew", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "year": {
            "id": "118118634930920", 
            "name": "2012"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "109363495748584", 
            "name": "University of California, Santa Cruz"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "type": "College"
        }
      ], 
      "id": "1559320789"
    }, 
    {
      "name": "Jonathan Teng", 
      "education": [
        {
          "school": {
            "id": "110939065597234", 
            "name": "MSJ"
          }, 
          "year": {
            "id": "118118634930920", 
            "name": "2012"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "75559051071", 
            "name": "California State University, Fullerton"
          }, 
          "type": "College"
        }
      ], 
      "id": "1561797125"
    }, 
    {
      "name": "Richard Liang", 
      "id": "1581280009"
    }, 
    {
      "name": "Valerie Hau", 
      "id": "1589295795"
    }, 
    {
      "name": "Stacey Chuang", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "year": {
            "id": "136328419721520", 
            "name": "2009"
          }, 
          "type": "High School", 
          "classes": [
            {
              "id": "161878910530139", 
              "name": "Class of 2012"
            }
          ]
        }, 
        {
          "school": {
            "id": "111873468830459", 
            "name": "Mt. Pleasant High School, San Jose, CA"
          }, 
          "year": {
            "id": "201638419856163", 
            "name": "2011"
          }, 
          "type": "High School", 
          "classes": [
            {
              "id": "161878910530139", 
              "name": "Class of 2012"
            }
          ]
        }, 
        {
          "school": {
            "id": "34410694953", 
            "name": "De Anza College"
          }, 
          "type": "College"
        }
      ], 
      "id": "1591175484"
    }, 
    {
      "name": "Hong Leong Share", 
      "id": "1594910768"
    }, 
    {
      "name": "Dinakar Guthy", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }
      ], 
      "id": "1603066707"
    }, 
    {
      "name": "Natalie Hoang", 
      "education": [
        {
          "school": {
            "id": "275087292600061", 
            "name": "Cupertino High School"
          }, 
          "type": "High School", 
          "classes": [
            {
              "id": "107512149278840", 
              "name": "Journalism", 
              "with": [
                {
                  "id": "594874457", 
                  "name": "Anthony Kao"
                }
              ], 
              "from": {
                "id": "594874457", 
                "name": "Anthony Kao"
              }
            }
          ]
        }, 
        {
          "school": {
            "id": "105735332794532", 
            "name": "Scripps College"
          }, 
          "year": {
            "id": "105576766163075", 
            "name": "2015"
          }, 
          "concentration": [
            {
              "id": "108180979203954", 
              "name": "Economics"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "1609726713"
    }, 
    {
      "name": "Daniel Phan", 
      "education": [
        {
          "school": {
            "id": "113972801946240", 
            "name": "Chadwick School"
          }, 
          "year": {
            "id": "118118634930920", 
            "name": "2012"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "103756122996046", 
            "name": "Pomona College"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "type": "College"
        }
      ], 
      "id": "1612933971"
    }, 
    {
      "name": "Anurag Reddy", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "10111634660", 
            "name": "UC Berkeley"
          }, 
          "type": "College"
        }
      ], 
      "id": "1617177534"
    }, 
    {
      "name": "Darren Li", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "11482933751", 
            "name": "UCSD Academic Connections"
          }, 
          "type": "College"
        }
      ], 
      "id": "1625175276"
    }, 
    {
      "name": "Eric Deng", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "55161634718", 
            "name": "Harvard Secondary School Program (SSP)"
          }, 
          "year": {
            "id": "118118634930920", 
            "name": "2012"
          }, 
          "type": "College", 
          "classes": [
            {
              "id": "191366244237053", 
              "name": "Introduction to Capital Markets and Investments"
            }, 
            {
              "id": "189778851055340", 
              "name": "Organizations, Management Behavior and Economics"
            }
          ]
        }
      ], 
      "id": "1626752792"
    }, 
    {
      "name": "Johnny Kitta", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "year": {
            "id": "118118634930920", 
            "name": "2012"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "11360325957", 
            "name": "UCLA"
          }, 
          "type": "College"
        }
      ], 
      "id": "1627685853"
    }, 
    {
      "name": "Frank Chen", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "year": {
            "id": "138879996141011", 
            "name": "2013"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "105495142817230", 
            "name": "University of California, Los Angeles"
          }, 
          "concentration": [
            {
              "id": "106166156082069", 
              "name": "Electrical Engineering"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "1629939337"
    }, 
    {
      "name": "Christian Lee", 
      "education": [
        {
          "school": {
            "id": "104154589622349", 
            "name": "Saratoga High School"
          }, 
          "year": {
            "id": "143641425651920", 
            "name": "2014"
          }, 
          "type": "High School"
        }
      ], 
      "id": "1638829913"
    }, 
    {
      "name": "Blair Crossman", 
      "education": [
        {
          "school": {
            "id": "114855481862914", 
            "name": "Coronado School of the Arts"
          }, 
          "year": {
            "id": "118118634930920", 
            "name": "2012"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "115668125113228", 
            "name": "Coronado High"
          }, 
          "year": {
            "id": "118118634930920", 
            "name": "2012"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "25827817664", 
            "name": "Pomona College"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "type": "College"
        }
      ], 
      "id": "1641400212"
    }, 
    {
      "name": "Monchen Kao", 
      "education": [
        {
          "school": {
            "id": "108212025867060", 
            "name": "Bellarmine College Preparatory"
          }, 
          "year": {
            "id": "115222815248992", 
            "name": "2012"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "8825331245", 
            "name": "Georgetown University"
          }, 
          "year": {
            "id": "105576766163075", 
            "name": "2015"
          }, 
          "concentration": [
            {
              "id": "109479582403827", 
              "name": "International Political Economy"
            }, 
            {
              "id": "111883932161088", 
              "name": "International Development"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "1644798507"
    }, 
    {
      "name": "Dimi Matcovschi", 
      "id": "1650501400"
    }, 
    {
      "name": "Roy Park", 
      "id": "1696254996"
    }, 
    {
      "name": "Matt Farby Farberov", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "year": {
            "id": "115222815248992", 
            "name": "2012"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "23680344606", 
            "name": "Arizona State University"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "concentration": [
            {
              "id": "112718455409766", 
              "name": "Criminal Justice"
            }
          ], 
          "type": "College", 
          "classes": [
            {
              "id": "182459431796117", 
              "name": "Class of 2016"
            }
          ]
        }
      ], 
      "id": "1708058175"
    }, 
    {
      "name": "Sean Li", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "year": {
            "id": "105576766163075", 
            "name": "2015"
          }, 
          "type": "High School", 
          "classes": [
            {
              "id": "134338529965010", 
              "name": "Class of 2015"
            }
          ]
        }, 
        {
          "school": {
            "id": "7093532993", 
            "name": "Ohlone College"
          }, 
          "type": "College"
        }
      ], 
      "id": "1722541976"
    }, 
    {
      "name": "Adam Homann", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "112271455455353", 
            "name": "San Jose State University"
          }, 
          "type": "College"
        }
      ], 
      "id": "1732791850"
    }, 
    {
      "name": "Edward Nguyen", 
      "id": "1755681364"
    }, 
    {
      "name": "Michael Shen", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "year": {
            "id": "105576766163075", 
            "name": "2015"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "College"
        }
      ], 
      "id": "1764870468"
    }, 
    {
      "name": "Kartik Surugucchi", 
      "education": [
        {
          "school": {
            "id": "103991312969759", 
            "name": "Mission San Jose High School"
          }, 
          "year": {
            "id": "115222815248992", 
            "name": "2012"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "113123972034419", 
            "name": "San Francisco State University"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "concentration": [
            {
              "id": "104096132959364", 
              "name": "Business"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "1770501148"
    }, 
    {
      "name": "Brennon Ng", 
      "education": [
        {
          "school": {
            "id": "351573841586647", 
            "name": "Mission San Jose High School"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }
      ], 
      "id": "1799071954"
    }, 
    {
      "name": "Nathan Hui", 
      "education": [
        {
          "school": {
            "id": "108034402563741", 
            "name": "Cupertino High"
          }, 
          "year": {
            "id": "118118634930920", 
            "name": "2012"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "108047109223278", 
            "name": "University of California, San Diego"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "concentration": [
            {
              "id": "106166156082069", 
              "name": "Electrical Engineering"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "1826127082"
    }, 
    {
      "name": "Wantong Liu", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "year": {
            "id": "118118634930920", 
            "name": "2012"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "113218455355218", 
            "name": "Chinese Christian Schools"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "87873693141", 
            "name": "Boston College"
          }, 
          "type": "College"
        }
      ], 
      "id": "1831329932"
    }, 
    {
      "name": "Justine Chan", 
      "id": "100000008832313"
    }, 
    {
      "name": "Shubham Agrawal", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "104328202999303", 
            "name": "UC San Diego"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "concentration": [
            {
              "id": "190872897600294", 
              "name": "Biochemistry and Cell Biology"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "100000041162710"
    }, 
    {
      "name": "Karen Normil", 
      "education": [
        {
          "school": {
            "id": "106083502756025", 
            "name": "Reading High School"
          }, 
          "year": {
            "id": "118118634930920", 
            "name": "2012"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "140998521533", 
            "name": "Brown University"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "type": "College"
        }
      ], 
      "id": "100000041455031"
    }, 
    {
      "name": "Bowei Liu", 
      "id": "100000042508571"
    }, 
    {
      "name": "Christopher Song", 
      "education": [
        {
          "school": {
            "id": "115668125113228", 
            "name": "Coronado High"
          }, 
          "year": {
            "id": "118118634930920", 
            "name": "2012"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "114855481862914", 
            "name": "Coronado School of the Arts"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "25827817664", 
            "name": "Pomona College"
          }, 
          "type": "College", 
          "classes": [
            {
              "id": "182459431796117", 
              "name": "Class of 2016"
            }
          ]
        }
      ], 
      "id": "100000048782254"
    }, 
    {
      "name": "Hannah Choi", 
      "education": [
        {
          "school": {
            "id": "107604129268675", 
            "name": "Hopkins Junior High School"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }
      ], 
      "id": "100000062297947"
    }, 
    {
      "name": "Brenda Garcia", 
      "education": [
        {
          "school": {
            "id": "110015655694880", 
            "name": "Elizabeth Learning Center"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "103756122996046", 
            "name": "Pomona College"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "type": "College", 
          "classes": [
            {
              "id": "182459431796117", 
              "name": "Class of 2016"
            }
          ]
        }
      ], 
      "id": "100000065958570"
    }, 
    {
      "name": "Henry Li", 
      "education": [
        {
          "school": {
            "id": "108037572550621", 
            "name": "Westmount High School"
          }, 
          "year": {
            "id": "201638419856163", 
            "name": "2011"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School", 
          "classes": [
            {
              "id": "188918704461958", 
              "name": "2012"
            }
          ]
        }, 
        {
          "school": {
            "id": "10111634660", 
            "name": "UC Berkeley"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "concentration": [
            {
              "id": "186196821414639", 
              "name": "Microbial Biology"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "100000074172413"
    }, 
    {
      "name": "Alex Chien", 
      "education": [
        {
          "school": {
            "id": "108212025867060", 
            "name": "Bellarmine College Preparatory"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "type": "High School"
        }
      ], 
      "id": "100000097808345"
    }, 
    {
      "name": "Masamichi Martin Fukui", 
      "education": [
        {
          "school": {
            "id": "112734332072619", 
            "name": "Palo Alto High School"
          }, 
          "year": {
            "id": "140617569303679", 
            "name": "2007"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "106538319376398", 
            "name": "University of California, Berkeley"
          }, 
          "year": {
            "id": "144044875610606", 
            "name": "2011"
          }, 
          "type": "College"
        }, 
        {
          "school": {
            "id": "107278102635060", 
            "name": "University of California, Hastings College of the Law"
          }, 
          "degree": {
            "id": "131847003547722", 
            "name": "Juris Doctor"
          }, 
          "year": {
            "id": "105576766163075", 
            "name": "2015"
          }, 
          "type": "Graduate School"
        }
      ], 
      "id": "100000109076445"
    }, 
    {
      "name": "China Lau", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School", 
          "classes": [
            {
              "id": "195573007135761", 
              "name": "2014"
            }
          ]
        }
      ], 
      "id": "100000119275074"
    }, 
    {
      "name": "William Zhao", 
      "education": [
        {
          "school": {
            "id": "351573841586647", 
            "name": "Mission San Jose High School"
          }, 
          "year": {
            "id": "118118634930920", 
            "name": "2012"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "114682278549347", 
            "name": "Uc irvine"
          }, 
          "type": "College"
        }
      ], 
      "id": "100000126370815"
    }, 
    {
      "name": "Brian Kim", 
      "education": [
        {
          "school": {
            "id": "104154589622349", 
            "name": "Saratoga High School"
          }, 
          "year": {
            "id": "138879996141011", 
            "name": "2013"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "10111634660", 
            "name": "UC Berkeley"
          }, 
          "type": "College"
        }
      ], 
      "id": "100000128111360"
    }, 
    {
      "name": "Kayla Kim", 
      "id": "100000128171360"
    }, 
    {
      "name": "Lindsey Gipson", 
      "education": [
        {
          "school": {
            "id": "110999155589058", 
            "name": "Everett High School"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "25827817664", 
            "name": "Pomona College"
          }, 
          "type": "College"
        }, 
        {
          "school": {
            "id": "106204622031", 
            "name": "Ocean Research College Academy"
          }, 
          "type": "College"
        }
      ], 
      "id": "100000128686344"
    }, 
    {
      "name": "Alex Wu", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "year": {
            "id": "143641425651920", 
            "name": "2014"
          }, 
          "type": "High School"
        }
      ], 
      "id": "100000141923301"
    }, 
    {
      "name": "Brian BRwu Wu", 
      "id": "100000165661086"
    }, 
    {
      "name": "Leo Estrada", 
      "education": [
        {
          "school": {
            "id": "106423856055772", 
            "name": "A. B. Miller High School"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "110678318959787", 
            "name": "Claremont Colleges"
          }, 
          "type": "College"
        }, 
        {
          "school": {
            "id": "103756122996046", 
            "name": "Pomona College"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "type": "College"
        }
      ], 
      "id": "100000170533551"
    }, 
    {
      "name": "Jack Fendell", 
      "education": [
        {
          "school": {
            "id": "103816116323649", 
            "name": "Bexley High School"
          }, 
          "year": {
            "id": "107638302624745", 
            "name": "1973"
          }, 
          "type": "High School"
        }
      ], 
      "id": "100000178696446"
    }, 
    {
      "name": "Jason Russell Amico", 
      "education": [
        {
          "school": {
            "id": "108058285894979", 
            "name": "Irvington High School"
          }, 
          "type": "High School", 
          "classes": [
            {
              "id": "195573007135761", 
              "name": "2014"
            }
          ]
        }
      ], 
      "id": "100000192702649"
    }, 
    {
      "name": "Bolun Liu", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "year": {
            "id": "118118634930920", 
            "name": "2012"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "145314775555853", 
            "name": "Yale University Class of 2016"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "type": "College"
        }
      ], 
      "id": "100000196132180"
    }, 
    {
      "name": "Jedrik Chao", 
      "id": "100000207491650"
    }, 
    {
      "name": "Ken Lai", 
      "education": [
        {
          "school": {
            "id": "108027849231742", 
            "name": "XiaYang QiaoYu High School"
          }, 
          "year": {
            "id": "102838599769236", 
            "name": "1979"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "103130999727767", 
            "name": "Xiamen University"
          }, 
          "year": {
            "id": "130747936967273", 
            "name": "1983"
          }, 
          "type": "College", 
          "classes": [
            {
              "id": "180833085287450", 
              "name": "Class of 1983"
            }
          ]
        }, 
        {
          "school": {
            "id": "55528788113", 
            "name": "University of Wisconsin-Madison"
          }, 
          "degree": {
            "id": "287037254666382", 
            "name": "Ph.D in Electrical Engineering"
          }, 
          "year": {
            "id": "137409666290034", 
            "name": "1995"
          }, 
          "type": "Graduate School"
        }, 
        {
          "school": {
            "id": "5652694310", 
            "name": "Michigan Technological University"
          }, 
          "degree": {
            "id": "109903862418964", 
            "name": "Master of Science"
          }, 
          "year": {
            "id": "136666673036069", 
            "name": "1987"
          }, 
          "type": "Graduate School"
        }
      ], 
      "id": "100000230056818"
    }, 
    {
      "name": "Bobby Xiong", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "107363709293503", 
            "name": "University of California, Irvine"
          }, 
          "type": "College"
        }
      ], 
      "id": "100000311713465"
    }, 
    {
      "name": "Mauricio Molina", 
      "education": [
        {
          "school": {
            "id": "111344202223030", 
            "name": "Valley High School"
          }, 
          "year": {
            "id": "144044875610606", 
            "name": "2011"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "110678318959787", 
            "name": "Claremont Colleges"
          }, 
          "concentration": [
            {
              "id": "104076956295773", 
              "name": "Computer Science"
            }
          ], 
          "type": "College"
        }, 
        {
          "school": {
            "id": "103756122996046", 
            "name": "Pomona College"
          }, 
          "year": {
            "id": "105576766163075", 
            "name": "2015"
          }, 
          "concentration": [
            {
              "id": "104076956295773", 
              "name": "Computer Science"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "100000388164475"
    }, 
    {
      "name": "Win Wu", 
      "id": "100000388445083"
    }, 
    {
      "name": "Brandon Fuhs", 
      "education": [
        {
          "school": {
            "id": "351573841586647", 
            "name": "Mission San Jose High School"
          }, 
          "year": {
            "id": "118118634930920", 
            "name": "2012"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "109364479082607", 
            "name": "University of Nevada, Reno"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "concentration": [
            {
              "id": "107512149278840", 
              "name": "Journalism"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "100000400428921"
    }, 
    {
      "name": "Dreamning Chin", 
      "id": "100000414935456"
    }, 
    {
      "name": "Lillian Wang", 
      "id": "100000421927487"
    }, 
    {
      "name": "Jeffrey Chen", 
      "education": [
        {
          "school": {
            "id": "104154589622349", 
            "name": "Saratoga High School"
          }, 
          "year": {
            "id": "143641425651920", 
            "name": "2014"
          }, 
          "type": "High School"
        }
      ], 
      "id": "100000431899110"
    }, 
    {
      "name": "Jimmy Guo", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "10111634660", 
            "name": "UC Berkeley"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "type": "College"
        }
      ], 
      "id": "100000491521818"
    }, 
    {
      "name": "Zemei Zee", 
      "education": [
        {
          "school": {
            "id": "109642382395535", 
            "name": "Monta Vista High School"
          }, 
          "type": "High School"
        }
      ], 
      "id": "100000505212981"
    }, 
    {
      "name": "Chetan Rane", 
      "education": [
        {
          "school": {
            "id": "108212025867060", 
            "name": "Bellarmine College Preparatory"
          }, 
          "year": {
            "id": "105576766163075", 
            "name": "2015"
          }, 
          "type": "High School"
        }
      ], 
      "id": "100000510452920"
    }, 
    {
      "name": "Morgan Scian", 
      "id": "100000545467392"
    }, 
    {
      "name": "Michelle Guo", 
      "id": "100000595119854"
    }, 
    {
      "name": "Maria Young", 
      "education": [
        {
          "school": {
            "id": "103756122996046", 
            "name": "Pomona College"
          }, 
          "type": "College"
        }
      ], 
      "id": "100000602056067"
    }, 
    {
      "name": "Hrishikesh Chary", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "year": {
            "id": "118118634930920", 
            "name": "2012"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "108047109223278", 
            "name": "University of California, San Diego"
          }, 
          "type": "College"
        }
      ], 
      "id": "100000606774370"
    }, 
    {
      "name": "Raghav Sharma", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "year": {
            "id": "118118634930920", 
            "name": "2012"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "10111634660", 
            "name": "UC Berkeley"
          }, 
          "concentration": [
            {
              "id": "105573196144184", 
              "name": "Electrical Engineering and Computer Science"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "100000720295154"
    }, 
    {
      "name": "Ashwin Shailesh", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "College"
        }
      ], 
      "id": "100000876321077"
    }, 
    {
      "name": "Trisha Srivastava", 
      "id": "100000880225560"
    }, 
    {
      "name": "Lin Luo", 
      "id": "100000894660987"
    }, 
    {
      "name": "Jennifer Feng", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }
      ], 
      "id": "100000899932238"
    }, 
    {
      "name": "Charley Chen", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }
      ], 
      "id": "100000899946683"
    }, 
    {
      "name": "John Wei", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "year": {
            "id": "144044875610606", 
            "name": "2011"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "106266172744997", 
            "name": "University of the Pacific"
          }, 
          "type": "College"
        }
      ], 
      "id": "100000944970647"
    }, 
    {
      "name": "Elliot Wuu", 
      "education": [
        {
          "school": {
            "id": "558083074234402", 
            "name": "Elliot Conservatory of Wuusic"
          }, 
          "year": {
            "id": "532490046771314", 
            "name": "2017"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "145141348909090", 
            "name": "Elliot Wuu School"
          }, 
          "year": {
            "id": "185588044800194", 
            "name": "2017"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "107604129268675", 
            "name": "Hopkins Junior High School"
          }, 
          "type": "High School", 
          "with": [
            {
              "id": "100002356630491", 
              "name": "Kenneth Leung"
            }
          ]
        }, 
        {
          "school": {
            "id": "107657982591044", 
            "name": "San Francisco Conservatory of Music"
          }, 
          "type": "College"
        }
      ], 
      "id": "100000955187630"
    }, 
    {
      "name": "Yashas Kumar", 
      "education": [
        {
          "school": {
            "id": "103991312969759", 
            "name": "Mission San Jose High School"
          }, 
          "year": {
            "id": "115222815248992", 
            "name": "2012"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "7133766387", 
            "name": "Carnegie Mellon University"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "concentration": [
            {
              "id": "104076956295773", 
              "name": "Computer Science"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "100000970085672"
    }, 
    {
      "name": "Andrew Jonathan Chang", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School", 
          "classes": [
            {
              "id": "180322765434933", 
              "name": "2015"
            }
          ]
        }
      ], 
      "id": "100001115524626"
    }, 
    {
      "name": "Emeri Zhang", 
      "education": [
        {
          "school": {
            "id": "106224342750379", 
            "name": "Hogwarts School of Witchcraft and Wizardry"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "107604129268675", 
            "name": "Hopkins Junior High School"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "College"
        }
      ], 
      "id": "100001115850384"
    }, 
    {
      "name": "Andrew Lee", 
      "id": "100001116392914"
    }, 
    {
      "name": "Isabella Costanza", 
      "education": [
        {
          "school": {
            "id": "110165395670851", 
            "name": "Henry M. Gunn High School"
          }, 
          "year": {
            "id": "143641425651920", 
            "name": "2014"
          }, 
          "type": "High School"
        }
      ], 
      "id": "100001255535372"
    }, 
    {
      "name": "Katherine Chang", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "year": {
            "id": "143641425651920", 
            "name": "2014"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "125931390766302", 
            "name": "N/A"
          }, 
          "type": "College"
        }
      ], 
      "id": "100001289080570"
    }, 
    {
      "name": "Maria Laura Arciniega", 
      "education": [
        {
          "school": {
            "id": "107884735911753", 
            "name": "Bassett Senior High"
          }, 
          "year": {
            "id": "118118634930920", 
            "name": "2012"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "103756122996046", 
            "name": "Pomona College"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "type": "College"
        }
      ], 
      "id": "100001304343290"
    }, 
    {
      "name": "Giovanni Pincilotti", 
      "education": [
        {
          "school": {
            "id": "103991312969759", 
            "name": "Mission San Jose High School"
          }, 
          "year": {
            "id": "118118634930920", 
            "name": "2012"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "7093532993", 
            "name": "Ohlone College"
          }, 
          "type": "College"
        }
      ], 
      "id": "100001337796416"
    }, 
    {
      "name": "Lauren Collins", 
      "education": [
        {
          "school": {
            "id": "110531435641986", 
            "name": "The Bishop's School"
          }, 
          "year": {
            "id": "201638419856163", 
            "name": "2011"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "103756122996046", 
            "name": "Pomona College"
          }, 
          "year": {
            "id": "105576766163075", 
            "name": "2015"
          }, 
          "concentration": [
            {
              "id": "109314462420288", 
              "name": "Biology"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "100001377797188"
    }, 
    {
      "name": "Albert Li", 
      "education": [
        {
          "school": {
            "id": "106614486041161", 
            "name": "Piedmont Hills High"
          }, 
          "year": {
            "id": "115222815248992", 
            "name": "2012"
          }, 
          "type": "High School", 
          "classes": [
            {
              "id": "188918704461958", 
              "name": "2012"
            }
          ]
        }, 
        {
          "school": {
            "id": "105930651606", 
            "name": "Harvard University"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "concentration": [
            {
              "id": "176344019076336", 
              "name": "Chemical and Physical Biology"
            }, 
            {
              "id": "103966102974293", 
              "name": "Mathematics"
            }
          ], 
          "type": "College", 
          "classes": [
            {
              "id": "182459431796117", 
              "name": "Class of 2016"
            }
          ]
        }
      ], 
      "id": "100001446955092"
    }, 
    {
      "name": "King Huang", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "year": {
            "id": "118118634930920", 
            "name": "2012"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "13917075214", 
            "name": "UC Davis"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "type": "College"
        }
      ], 
      "id": "100001529183434"
    }, 
    {
      "name": "Sophie Wang", 
      "education": [
        {
          "school": {
            "id": "115348735145105", 
            "name": "Palo Alto High"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "112734332072619", 
            "name": "Palo Alto High School"
          }, 
          "year": {
            "id": "118118634930920", 
            "name": "2012"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "18058830773", 
            "name": "Princeton University"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "type": "College"
        }
      ], 
      "id": "100001535597076"
    }, 
    {
      "name": "Walton Zhang", 
      "education": [
        {
          "school": {
            "id": "103815889656540", 
            "name": "Shenzhen Foreign Languages School"
          }, 
          "year": {
            "id": "118118634930920", 
            "name": "2012"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "103756122996046", 
            "name": "Pomona College"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "type": "College"
        }
      ], 
      "id": "100001583832978"
    }, 
    {
      "name": "Karen Hsu", 
      "id": "100001595332563"
    }, 
    {
      "name": "Krishan Oliver Kumar", 
      "education": [
        {
          "school": {
            "id": "108546012510012", 
            "name": "The Harker School"
          }, 
          "year": {
            "id": "143641425651920", 
            "name": "2014"
          }, 
          "type": "High School"
        }
      ], 
      "id": "100001722818612"
    }, 
    {
      "name": "Jasmine Chau", 
      "id": "100001735168838"
    }, 
    {
      "name": "Richard Zhang", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "8570160131", 
            "name": "Cornell University"
          }, 
          "type": "College"
        }
      ], 
      "id": "100001798985315"
    }, 
    {
      "name": "Anjan Balgovind", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "year": {
            "id": "118118634930920", 
            "name": "2012"
          }, 
          "type": "High School"
        }
      ], 
      "id": "100001878794133"
    }, 
    {
      "name": "Vineet Jain", 
      "id": "100002123698198"
    }, 
    {
      "name": "Eric Jang", 
      "education": [
        {
          "school": {
            "id": "275087292600061", 
            "name": "Cupertino High School"
          }, 
          "year": {
            "id": "115222815248992", 
            "name": "2012"
          }, 
          "type": "High School", 
          "classes": [
            {
              "id": "107512149278840", 
              "name": "Journalism"
            }
          ]
        }, 
        {
          "school": {
            "id": "140998521533", 
            "name": "Brown University"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "type": "College"
        }
      ], 
      "id": "100002253624840"
    }, 
    {
      "name": "Kenneth Leung", 
      "education": [
        {
          "school": {
            "id": "103991312969759", 
            "name": "Mission San Jose High School"
          }, 
          "year": {
            "id": "185588044800194", 
            "name": "2017"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "107604129268675", 
            "name": "Hopkins Junior High School"
          }, 
          "year": {
            "id": "138879996141011", 
            "name": "2013"
          }, 
          "type": "High School", 
          "with": [
            {
              "id": "100002661104127", 
              "name": "Tanushri Sundar"
            }, 
            {
              "id": "1846129269", 
              "name": "Kevin Hom"
            }, 
            {
              "id": "100001964626782", 
              "name": "Fefe Li"
            }, 
            {
              "id": "100001606880264", 
              "name": "Christina Kruglikov"
            }, 
            {
              "id": "100001187057410", 
              "name": "Sunny Pasumarthi"
            }, 
            {
              "id": "100002305945530", 
              "name": "Ethan Farrington"
            }, 
            {
              "id": "100000288048140", 
              "name": "Evan Wong"
            }, 
            {
              "id": "1140242769", 
              "name": "Adil Bari"
            }, 
            {
              "id": "100000985330417", 
              "name": "Amy Wang"
            }, 
            {
              "id": "100002764571378", 
              "name": "Lilian Joy Feng"
            }, 
            {
              "id": "100000222463931", 
              "name": "Stephen Tselikov"
            }, 
            {
              "id": "100000439643965", 
              "name": "Eric Dang"
            }, 
            {
              "id": "100000460166175", 
              "name": "Kiet Nguyen"
            }, 
            {
              "id": "100000402054810", 
              "name": "Chris Kwok"
            }, 
            {
              "id": "1156627340", 
              "name": "James Qiao"
            }, 
            {
              "id": "100000689136569", 
              "name": "Joshua Ngo"
            }, 
            {
              "id": "100000547341059", 
              "name": "Cherlene Hoei"
            }, 
            {
              "id": "100001248456812", 
              "name": "Karen Trinh"
            }, 
            {
              "id": "100001126243607", 
              "name": "Makenna Fong"
            }, 
            {
              "id": "100000955395818", 
              "name": "Dhiva Krishna"
            }, 
            {
              "id": "100001563805469", 
              "name": "Sarah Deng"
            }, 
            {
              "id": "100000003344456", 
              "name": "Aarsh Shah"
            }, 
            {
              "id": "1840430857", 
              "name": "Kelly Shi"
            }, 
            {
              "id": "100002521997428", 
              "name": "Seema Saini"
            }, 
            {
              "id": "100001773541792", 
              "name": "Sarah Chen"
            }, 
            {
              "id": "100001549432330", 
              "name": "Vik Avantsa"
            }, 
            {
              "id": "100001208557191", 
              "name": "Anita Carraher"
            }, 
            {
              "id": "100000107393457", 
              "name": "Hansie Anirudhan"
            }, 
            {
              "id": "100002068099335", 
              "name": "Fendy Gao"
            }, 
            {
              "id": "100000196421480", 
              "name": "Lilian Joy Feng"
            }, 
            {
              "id": "100000554593677", 
              "name": "Yoobin Seo"
            }, 
            {
              "id": "100001778041670", 
              "name": "Jason Yu"
            }, 
            {
              "id": "100001055450745", 
              "name": "Tiffany Basrai"
            }, 
            {
              "id": "100000791281592", 
              "name": "Radhika Joshi"
            }, 
            {
              "id": "100000746334275", 
              "name": "Romir Desai"
            }, 
            {
              "id": "1394126401", 
              "name": "Yoobin Ricky Seo"
            }, 
            {
              "id": "100000628150579", 
              "name": "Rudy Estrada "
            }, 
            {
              "id": "100000589775643", 
              "name": "Roy Ho"
            }, 
            {
              "id": "100001275012346", 
              "name": "Eunice Min"
            }, 
            {
              "id": "100002271687510", 
              "name": "Ethan Lam"
            }, 
            {
              "id": "100000955187630", 
              "name": "Elliot Wuu"
            }, 
            {
              "id": "100000365486124", 
              "name": "Erik Wong"
            }, 
            {
              "id": "100000045235284", 
              "name": "William Neo"
            }, 
            {
              "id": "100000337054963", 
              "name": "Junior Wei"
            }, 
            {
              "id": "1811091324", 
              "name": "Savana Wang"
            }, 
            {
              "id": "100000221732369", 
              "name": "Jeff Wang"
            }, 
            {
              "id": "100000538413078", 
              "name": "Andy Wu"
            }, 
            {
              "id": "1841331016", 
              "name": "Nicholas Wen"
            }, 
            {
              "id": "1595977196", 
              "name": "Anthony Watkins"
            }
          ]
        }, 
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "College"
        }
      ], 
      "id": "100002356630491"
    }, 
    {
      "name": "Jonathan Chen", 
      "id": "100002380678714"
    }, 
    {
      "name": "Morgan Wu", 
      "education": [
        {
          "school": {
            "id": "109748892385588", 
            "name": "Lynbrook High School"
          }, 
          "year": {
            "id": "532490046771314", 
            "name": "2017"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "108369699187936", 
            "name": "Miller Middle School"
          }, 
          "type": "High School"
        }
      ], 
      "id": "100002392094341"
    }, 
    {
      "name": "Simone Prince-Eichner", 
      "education": [
        {
          "school": {
            "id": "249840305034365", 
            "name": "Home-Schooled, Sehome High School"
          }, 
          "year": {
            "id": "138879996141011", 
            "name": "2013"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "103756122996046", 
            "name": "Pomona College"
          }, 
          "type": "College"
        }
      ], 
      "id": "100002394125682"
    }, 
    {
      "name": "Erik Wu", 
      "education": [
        {
          "school": {
            "id": "109302495755269", 
            "name": "Bergen County Academies"
          }, 
          "year": {
            "id": "105576766163075", 
            "name": "2015"
          }, 
          "type": "High School"
        }
      ], 
      "id": "100002543788605"
    }, 
    {
      "name": "Boyu Liu", 
      "education": [
        {
          "school": {
            "id": "111774365506149", 
            "name": "Beijing No.4 High School"
          }, 
          "year": {
            "id": "118118634930920", 
            "name": "2012"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "103119943060893", 
            "name": "Claremont McKenna College"
          }, 
          "type": "College"
        }, 
        {
          "school": {
            "id": "25827817664", 
            "name": "Pomona College"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "type": "College", 
          "classes": [
            {
              "id": "170481426331222", 
              "name": "2016"
            }
          ]
        }
      ], 
      "id": "100002589184936"
    }, 
    {
      "name": "Candice Tandiono", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "year": {
            "id": "118118634930920", 
            "name": "2012"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "108619679169559", 
            "name": "UC Davis"
          }, 
          "type": "College"
        }, 
        {
          "school": {
            "id": "112199395458691", 
            "name": "University of California, Davis"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "concentration": [
            {
              "id": "174939082551488", 
              "name": "Biological Sciences/Pre-Med"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "100002696827518"
    }, 
    {
      "name": "Priya Magdalene", 
      "education": [
        {
          "school": {
            "id": "177467392271924", 
            "name": "Campbell Hall"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "103756122996046", 
            "name": "Pomona College"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "concentration": [
            {
              "id": "154284401291284", 
              "name": "Media Studies"
            }
          ], 
          "type": "College", 
          "classes": [
            {
              "id": "170481426331222", 
              "name": "2016"
            }
          ]
        }
      ], 
      "id": "100002733705889"
    }, 
    {
      "name": "Stella Han", 
      "education": [
        {
          "school": {
            "id": "103991312969759", 
            "name": "Mission San Jose High School"
          }, 
          "year": {
            "id": "105576766163075", 
            "name": "2015"
          }, 
          "type": "High School"
        }
      ], 
      "id": "100002773968108"
    }, 
    {
      "name": "Jo Melville", 
      "id": "100002973175633"
    }, 
    {
      "name": "John Herman", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "type": "High School", 
          "classes": [
            {
              "id": "188918704461958", 
              "name": "2012"
            }
          ]
        }, 
        {
          "school": {
            "id": "108159075873142", 
            "name": "Pohang University of Science and Technology"
          }, 
          "degree": {
            "id": "170434169669210", 
            "name": "PhD"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "concentration": [
            {
              "id": "141897375872318", 
              "name": "University"
            }, 
            {
              "id": "108213575873147", 
              "name": "Technology"
            }, 
            {
              "id": "108196582538810", 
              "name": "Science"
            }
          ], 
          "type": "Graduate School"
        }
      ], 
      "id": "100002988589145"
    }, 
    {
      "name": "David Tang", 
      "education": [
        {
          "school": {
            "id": "114841535196507", 
            "name": "Mission San Jose High"
          }, 
          "year": {
            "id": "120960561375312", 
            "name": "2013"
          }, 
          "type": "High School"
        }
      ], 
      "id": "100003492368648"
    }, 
    {
      "name": "Abdelwahab Bourai", 
      "id": "100003599817486"
    }, 
    {
      "name": "Lucia Liu", 
      "education": [
        {
          "school": {
            "id": "107705972591905", 
            "name": "Thomas Jefferson High School for Science and Technology"
          }, 
          "year": {
            "id": "118118634930920", 
            "name": "2012"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "22922516119", 
            "name": "Virginia Commonwealth University"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "concentration": [
            {
              "id": "166993813358651", 
              "name": "Painting & Printmaking"
            }
          ], 
          "type": "College", 
          "classes": [
            {
              "id": "182459431796117", 
              "name": "Class of 2016"
            }
          ]
        }
      ], 
      "id": "100003713695791"
    }, 
    {
      "name": "Laura Pandori", 
      "education": [
        {
          "school": {
            "id": "106261869412492", 
            "name": "Notre Dame High School, San Jose, CA"
          }, 
          "year": {
            "id": "118118634930920", 
            "name": "2012"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "25827817664", 
            "name": "Pomona College"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "type": "College"
        }
      ], 
      "id": "100003802695407"
    }, 
    {
      "name": "Vivian Chen", 
      "education": [
        {
          "school": {
            "id": "103756122996046", 
            "name": "Pomona College"
          }, 
          "type": "College"
        }
      ], 
      "id": "100004046600024"
    }, 
    {
      "name": "Tim Kung", 
      "education": [
        {
          "school": {
            "id": "108339569186839", 
            "name": "Westview High School"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "103756122996046", 
            "name": "Pomona College"
          }, 
          "type": "College"
        }
      ], 
      "id": "100004103893817"
    }, 
    {
      "name": "Geeny Moon", 
      "education": [
        {
          "school": {
            "id": "140942459303812", 
            "name": "Rangi Ruru Girls' School"
          }, 
          "year": {
            "id": "105576766163075", 
            "name": "2015"
          }, 
          "type": "High School"
        }
      ], 
      "id": "100004880225979"
    }, 
    {
      "name": "Thomas Feng", 
      "education": [
        {
          "school": {
            "id": "103991312969759", 
            "name": "Mission San Jose High School"
          }, 
          "year": {
            "id": "594629830562059", 
            "name": "2012"
          }, 
          "type": "High School"
        }, 
        {
          "school": {
            "id": "11360325957", 
            "name": "UCLA"
          }, 
          "year": {
            "id": "127342053975510", 
            "name": "2016"
          }, 
          "concentration": [
            {
              "id": "109823779047223", 
              "name": "Music Composition"
            }
          ], 
          "type": "College"
        }
      ], 
      "id": "100005484488731"
    }
  ]
for datum in data:
    try:
        schools = datum["education"]
    except: 
        schools = []
    for school in schools:
        if school["type"] == "College":
            college = school["school"]["name"]
        else : college = ""
    u = User(datum["name"].replace(" ",""),datum["name"].replace(" ","")+"@apployment.com","password",datum["name"],college)
    db.session.add(u)
db.session.commit()


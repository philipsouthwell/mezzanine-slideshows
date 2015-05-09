var opts = {
        //auto-advancing slides? accepts boolean (true/false) or object
        auto : {
            // speed to advance slides at. accepts number of milliseconds
            speed : 2500,
            // pause advancing on mouseover? accepts boolean
            pauseOnHover : true
        },
        // show fullscreen toggle? accepts boolean
        fullScreen : true,
        // support swiping on touch devices? accepts boolean, requires hammer.js
        swipe : true
    };
makeBSS('.better-simple-slideshow', opts);
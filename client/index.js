function mapLocation() {
    var directionsDisplay;
    var directionsService = new google.maps.DirectionsService();
    var map;
    var locations = [];

    function initialize() {
        directionsDisplay = new google.maps.DirectionsRenderer();
        var lima = new google.maps.LatLng(-12.111370, -77.012041);
        var mapOptions = {
            zoom: 15,
            center: lima
        };
        map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);
        directionsDisplay.setMap(map);
        google.maps.event.addDomListener(document.getElementById('routebtn'), 'click', calcRoute);
        map.addListener('click', function (e) {
            placeMarker(e.latLng, map);
        });

        function placeMarker(position, map) {
            var marker = new google.maps.Marker({
                position: position,
                map: map
            });
            map.panTo(position);
            console.log(position.lat().toFixed(3), position.lng().toFixed(3));
            locations.push(position);
        }
        var start = new google.maps.LatLng(-12.113468, -77.026075);
        var end = new google.maps.LatLng(-12.132097, -76.979512);

        // var startMarker = new google.maps.Marker({
        //     position: start,
        //     map: map,
        //     draggable: true
        // });
        // var endMarker = new google.maps.Marker({
        //     position: end,
        //     map: map,
        //     draggable: true
        // });

    }

    function calcRoute() {
        // var start = new google.maps.LatLng(-12.113468, -77.026075);
        //var end = new google.maps.LatLng(38.334818, -181.884886);
        // var end = new google.maps.LatLng(-12.132097, -76.979512);

        /* var startMarker = new google.maps.Marker({
                    position: start,
                    map: map,
                    draggable: true
                });
                var endMarker = new google.maps.Marker({
                    position: end,
                    map: map,
                    draggable: true
                }); */

        if (directionsDisplay != null) {
            directionsDisplay.setMap(null);
            directionsDisplay = null;
        }

        for (var i = 0; i < locations.length - 1; i++) {

            // var bounds = new google.maps.LatLngBounds();
            var start = new google.maps.LatLng(locations[i].lat(), locations[i].lng());
            var end = new google.maps.LatLng(locations[i + 1].lat(), locations[i + 1].lng());
            // bounds.extend(start);
            // bounds.extend(end);
            // map.fitBounds(bounds);
            // var request = {
            //     origin: start,
            //     destination: end,
            //     travelMode: google.maps.TravelMode.DRIVING
            // };
            // directionsService.route(request, function (response, status) {
            //     if (status == google.maps.DirectionsStatus.OK) {
            //         // directionsDisplay = new google.maps.DirectionsRenderer();
            //         // directionsDisplay.setDirections(response);
            //         // directionsDisplay.setMap(map);
            //         // directionsDisplay = null;


            //     } else {
            //         alert("Directions Request from " + start.toUrlValue(6) + " to " + end.toUrlValue(6) + " failed: " + status);
            //     }
            // });
            var flightPath = new google.maps.Polyline({
                path: [start, end],
                geodesic: true,
                strokeColor: '#FF0000',
                strokeOpacity: 1.0,
                strokeWeight: 3,
                travelMode: google.maps.TravelMode.DRIVING
            });

            flightPath.setMap(map);

        }


    }

    google.maps.event.addDomListener(window, 'load', initialize);
}
mapLocation();



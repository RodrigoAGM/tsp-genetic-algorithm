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

    }

    function calcRoute() {

        var flightPath = new google.maps.Polyline({
            path: locations,
            geodesic: true,
            strokeColor: '#FF0000',
            strokeOpacity: 1.0,
            strokeWeight: 5,
            travelMode: google.maps.TravelMode.DRIVING
        });
        flightPath.setMap(map);
    }

    google.maps.event.addDomListener(window, 'load', initialize);
}
mapLocation();



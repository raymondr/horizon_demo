var w = null,
    h = 500,
    mouse = [null, null],
    fill = d3.scale.linear().domain([0, 1e4]).range(["brown", "steelblue"]);

$(function () {
  w = $("#vis").width() - 10;

  // Initialise boids.
  var boids = new Array();

  $.ajax({
    url: window.location,
    dataType: "json",
    success: function (data, textStatus, jqXHR) {
      $.each(data, function (index, obj) {
        var b = boid().position([Math.random() * w, Math.random() * h])
                      .velocity([Math.random() * 2 -1, Math.random() * 2 -1])
                      .maxSpeed(obj.flavor.vcpus / 2)
                      .desiredSeparation(obj.flavor.ram / 16 + 2);
        b.instance = obj;
        boids.push(b);
      });
      init_flocking();
    }
  });

  function init_flocking() {
    // Compute initial positions.
    var vertices = boids.map(function(boid) {
      return boid(boids);
    });

    d3.select(window).on("blur", nullGravity);

    var svg = d3.select("#vis")
      .append("svg")
        .attr("width", w)
        .attr("height", h)
        .attr("class", "PiYG")
        .on("mousemove", function() {
          var m = d3.mouse(this);
          mouse[0] = m[0];
          mouse[1] = m[1];
        })
        .on("mouseout", nullGravity);

    /* I don't like this.
    svg.selectAll("path")
        .data(d3.geom.voronoi(vertices))
      .enter().append("path")
        .attr("class", function(d, i) { return i ? "q" + (i % 9) + "-9" : null; })
        .attr("d", function(d) { return "M" + d.join("L") + "Z"; });
    */

    svg.selectAll("circle")
        .data(vertices)
      .enter().append("circle")
        .attr("transform", function(d) { return "translate(" + d + ")"; })
        .attr("r", 5);

    d3.timer(function() {
      // Update boid positions.
      boids.forEach(function(boid, i) {
        vertices[i] = boid(boids);
      });

      // Update circle positions.
      svg.selectAll("circle")
          .data(vertices)
          .attr("transform", function(d) { return "translate(" + d + ")"; });

      // Set the sizes
      svg.selectAll("circle")
          .data(boids)
          .attr("r", function(boid) {
            return boid.instance.flavor.ram / 16 + 5; }
          );

      /* I don't like this either.
      // Update voronoi diagram.
      svg.selectAll("path")
          .data(d3.geom.voronoi(vertices))
          .attr("d", function(d) { return "M" + d.join("L") + "Z"; })
          .style("fill", function(d) { return fill((d3.geom.polygon(d).area())); });
      */
    });
  }

  function nullGravity() {
    mouse[0] = mouse[1] = null;
  }
});

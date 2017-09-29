<div id="pixelgrid"></div>
<style type="text/css">
	.square 
	{
	    display: table-cell;
	    vertical-align: middle;
	    text-align: center;
	    
	    height: 2.5rem;
	    width: 2.5rem;
	    background-color: white;
	}
</style>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
<script type="text/javascript"
    src="https://cdn.rawgit.com/brython-dev/brython/stable/www/src/brython.js">
</script>
<script type="text/python">
	col = [24.5, 24.0, 23.5, 23.75, 23.5, 24.0, 24.0, 24.25, 24.0, 24.0, 23.75, 23.75, 23.5, 24.5, 24.75, 24.75, 24.25, 25.5, 24.75, 32.25, 25.5, 22.0, 26.25, 31.25, 24.5, 24.75, 28.25, 30.25, 30.25, 30.0, 30.25, 30.0, 23.75, 24.25, 26.25, 28.5, 30.25, 31.0, 30.75, 29.75, 23.75, 23.5, 24.0, 24.75, 25.25, 28.0, 29.25, 29.25, 23.5, 23.5, 23.75, 24.25, 24.5, 28.0, 29.5, 30.5, 23.5, 24.0, 23.5, 23.5, 23.75, 26.0, 28.75, 30.0]s
</script>
<script type="text/javascript">
	var tocol = function (num) {
		var norm = (num - 15) / 28;
	    var val = (norm * 255);
	    val = Math.ceil(val);
	    var antival = 255 - val;
	    
	    val = val.toString(16);
	    antival = antival.toString(16);
	    
	    if (val.length == 1) {
	    		val = "0" + val;
	    }
	    
	    if (antival.length == 1) {
	    		antival = "0" + antival;
	    }
	    
	    return "#" + val + "00" + antival;
	};

	var inner = "";
	for (i = 0; i < 8; i++) 
	{
	    var row = '<div>';
	    
	    for (j = 0; j < 8; j++)
	        row += '<div class="square" style="background:' + tocol(col[8 * i + j]) + '"></div>';
	    
	    row += '</div>';
	    
	    inner.append(row);
	}

	document.getElementById('pixelgrid').innerHTML = inner;
</script>
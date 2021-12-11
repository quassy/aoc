<?php

define("REPEAT_COUNT", 1);
define("UNIT_FACTOR", 1000);
define("UNIT", "ms");


function time_loop(?int $count = REPEAT_COUNT): Generator {
    # Generator to measure execution time of a code block in a for loop.
    $count = max(abs($count), 1);

    $start = microtime(true);
    for ($i=0; $i < $count; $i++) {
        yield null;
    }
    $end = microtime(true);
    $duration = ($end - $start) / floatval($count);
    echo("loop took ".$duration * UNIT_FACTOR." ".UNIT." (average of $count runs)\n");
    return $duration;
}


if (!debug_backtrace()) {
    foreach (time_loop(1000) as $_) {
        usleep(0.01 * 1e6);
    }
}

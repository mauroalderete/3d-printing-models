# retraction

Contains a STL model that I often use it to calibrate the retraction feature.
The retraction configure has [many aspect](https://help.prusa3d.com/article/stringing-and-oozing_1805) but only two are more important: `Lenght`, and `Retraction Speed`.

The procediments is easy:

## Preparation
Prepare many gcode using the STL model each one with diferents distribution of value for both variables. For example I should prepare print probes to:

| Probe ID | Lenght | Retraction Speed |
| -------- | ------ | ---------------- |
| A        | 40     | 2                |
| B        | 60     | 2                |
| C        | 60     | 1                |
| D        | 100    | 1                |
| E        | 30     | 1.5              |
| F        | 80     | 1.5              |
| G        | 30     | 0.5              |
| H        | 80     | 0.5              |
| I        | 15     | 0.75             |
| J        | 45     | 0.25             |

## Comparative

One time that I have all models printed and marked, I made a comparative to quality between results. Some prints will are better that others. I build a scale to order the models from bad to good.

## Metrics

There are many way of establishment metrics to determine the influence of the variables in the quality results.

One way, that results me better, is makes a double input sqaure and fix points to comparative pieces result.

For example, if the piece A is better that piece B then the piece A gain two points and write in the graph like:

This points can be:

- if a piece is better that another then gain 2 points
- if a piece see equal that another then gain 1 points
- if a piece see bader that another then doesn't gain points

Following this rules We can complete a graph like:

|     | A   | B   | C   | D   | E   | F   | G   | H   | I   | J   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A   | 0   | 2   | 0   | 1   | 2   | 2   | 0   | 0   | 1   | 0   |
| B   | 0   | 0   | 0   | 0   | 2   | 2   | 0   | 0   | 0   | 0   |
| C   | 2   | 2   | 0   | 2   | 2   | 2   | 0   | 0   | 2   | 1   |
| D   | 1   | 2   | 0   | 0   | 2   | 1   | 0   | 0   | 1   | 0   |
| E   | 0   | 1   | 0   | 0   | 0   | 0   | 0   | 0   | 0   | 0   |
| F   | 2   | 2   | 1   | 2   | 2   | 0   | 0   | 0   | 2   | 1   |
| G   | 2   | 2   | 2   | 2   | 2   | 2   | 0   | 0   | 2   | 2   |
| H   | 2   | 2   | 2   | 2   | 2   | 2   | 0   | 0   | 2   | 2   |
| I   | 1   | 2   | 0   | 1   | 2   | 0   | 0   | 0   | 0   | 0   |
| J   | 2   | 2   | 1   | 2   | 2   | 1   | 0   | 0   | 2   | 0   |

> The places that compare the same pieces contains 0 points.

For last, We add all point to each probe and atachment the result as a new column in the preparation table

| Probe ID | Lenght | Retraction Speed | Quality |
| -------- | ------ | ---------------- | ------- |
| A        | 40     | 2                | 6       |
| B        | 60     | 2                | 2       |
| C        | 60     | 1                | 12      |
| D        | 100    | 1                | 6       |
| E        | 30     | 1.5              | 1       |
| F        | 80     | 1.5              | 12      |
| G        | 30     | 0.5              | 16      |
| H        | 80     | 0.5              | 16      |
| I        | 15     | 0.75             | 6       |
| J        | 45     | 0.25             | 11      |

## Analyze and Predict

With the retuls quality table we can made a file to easily his the processing. Something like that [data.csv](src/data.csv).

Each line contains a probe metric. The first element is the `Retraction Speed`, the second is the `Lenght` and the last is the `Quality`. All separated by a comma.

```csv
40,2,4
60,2,2
60,1,12
100,1,5
30,1.5,1
80,1.5,12
30,0.5,16
80,0.5,16
15,0.75,6
45,0.25,11
```

This repo contains a small python script that helps you to view the result of the probes and determine the most optimal value to `Retraction Speed` and `Lenght` variables.

To run only execute in a bash terminal

```sh
python3 dispersion-viewer.py -f data.csv
```

For this example, a potential configure values could be:
- `Retraction Speed = 55 mm/s`
- `Lenght = 0.5 mm`

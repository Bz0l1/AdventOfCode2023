use std::io::{self, BufRead};
use std::fs::File;
use std::path::Path;

fn read_file() -> io::Result<Vec<String>> {
    let path = Path::new("./src/input.txt");
    let file = File::open(&path)?;
    let reader = io::BufReader::new(file);

    reader.lines().collect()
}

fn part1(lines: Vec<String>) -> i32 {
    let mut total_sum = 0;

    for line in lines {
        let parts: Vec<&str> = line.split(": ").collect();
        let game_id: i32 = parts[0].replace("Game ", "").parse().unwrap();
        let sets = parts[1].split("; ");

        let mut is_possible = true;

        for set in sets {
            let cubes: Vec<&str> = set.split(", ").collect();
            let mut red = 0;
            let mut green = 0;
            let mut blue = 0;

            for cube in &cubes {
                let parts: Vec<&str> = cube.split(' ').collect();
                let count: i32 = parts[0].parse().unwrap();
                match parts[1] {
                    "red" => red += count,
                    "green" => green += count,
                    "blue" => blue += count,
                    _ => {}
                }

                if red > 12 || green > 13 || blue > 14 {
                    is_possible = false;
                    break;
                }
            }
        }

        if is_possible {
            total_sum += game_id;
        }
    }

    total_sum
}

fn part2(lines: Vec<String>) -> i32 {
    let mut total_sum = 0;

    for line in lines {
        let parts: Vec<&str> = line.split(": ").collect();
        let sets = parts[1].split("; ");

        let mut max_red = 0;
        let mut max_green = 0;
        let mut max_blue = 0;

        for set in sets {
            let cubes: Vec<&str> = set.split(", ").collect();
            let mut red = 0;
            let mut green = 0;
            let mut blue = 0;

            for cube in &cubes {
                let parts: Vec<&str> = cube.split(' ').collect();
                let count: i32 = parts[0].parse().unwrap();
                match parts[1] {
                    "red" => red += count,
                    "green" => green += count,
                    "blue" => blue += count,
                    _ => {}
                }
            }

            max_red = max_red.max(red);
            max_green = max_green.max(green);
            max_blue = max_blue.max(blue);
        }

        let power = max_red * max_green * max_blue;
        total_sum += power;
    }

    total_sum
}

fn main() -> io::Result<()> {
    let lines = read_file()?;
    let mut total_sum = part1(lines.clone());
    println!("Part 1: {}", total_sum);

    total_sum = part2(lines.clone());
    println!("Part 2: {}", total_sum);

    Ok(())
}

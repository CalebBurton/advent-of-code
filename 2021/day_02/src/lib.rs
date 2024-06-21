use std::fs;

pub fn puzzle_a() {
    println!("\n\n==== Day 02 ====");
    println!("-- Puzzle A --");
    // ------------------------------------------------------------------------

    let contents = fs::read_to_string("day_02/02_input.txt").unwrap();
    let position = find_position(&contents);
    let result = position.horizontal * position.depth;

    println!("Result:\n{:?}", result);

    // ------------------------------------------------------------------------
}

struct Position {
    horizontal: i32,
    depth: i32,
}

fn find_position<'a>(input: &'a str) -> Position {
    let mut position = Position {
        horizontal: 0,
        depth: 0,
    };
    for line in input.lines() {
        let vec: Vec<&str> = line.split(" ").collect();
        let direction = vec[0];
        let distance: i32 = vec[1].parse().unwrap();

        match direction {
            "forward" => {
                position.horizontal += distance;
            }
            "down" => {
                position.depth += distance;
            }
            "up" => {
                position.depth -= distance;
            }
            _ => {
                panic!()
            }
        }
    }
    return position;
}

pub fn puzzle_b() {
    println!("\n-- Puzzle B --");
    // ------------------------------------------------------------------------

    let contents = fs::read_to_string("day_02/02_input.txt").unwrap();
    let position = find_position_b(&contents);
    let result = position.horizontal * position.depth;

    println!("Result:\n{:?}", result);

    // ------------------------------------------------------------------------
}

fn find_position_b<'a>(input: &'a str) -> Position {
    let mut position = Position {
        horizontal: 0,
        depth: 0,
    };
    let mut aim = 0;
    for line in input.lines() {
        let vec: Vec<&str> = line.split(" ").collect();
        let direction = vec[0];
        let distance: i32 = vec[1].parse().unwrap();

        match direction {
            "forward" => {
                position.horizontal += distance;
                position.depth += distance * aim;
            }
            "down" => {
                aim += distance;
            }
            "up" => {
                aim -= distance;
            }
            _ => {
                panic!()
            }
        }
    }
    return position;
}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn puzzle_a() {
        let contents = fs::read_to_string("day_02/02_test_input.txt").unwrap();
        let result = find_position(&contents);
        assert_eq!(result.horizontal, 15);
        assert_eq!(result.depth, 10);
    }
    #[test]
    fn puzzle_b() {
        let contents = fs::read_to_string("day_02/02_test_input.txt").unwrap();
        let result = find_position_b(&contents);
        assert_eq!(result.horizontal, 15);
        assert_eq!(result.depth, 60);
    }
}

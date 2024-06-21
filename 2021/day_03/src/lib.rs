// use regex::Regex;
use std::fs;

pub fn puzzle_a() {
    println!("\n\n==== Day 03 ====");
    println!("-- Puzzle A --");
    // ------------------------------------------------------------------------

    let contents = fs::read_to_string("day_03/input.txt").unwrap();
    let result = find_rates(&contents);

    println!("Result:\n{:?}", result);

    // ------------------------------------------------------------------------
}

// struct Position {
//     horizontal: i32,
//     depth: i32,
// }

fn find_rates<'a>(input: &'a str) -> i32 {
    // let seperator = Regex::new(r"([\d]+)").expect("Invalid regex");
    // let mut gamma = 0;
    // let mut epsilon = 0;
    for line in input.lines() {
        let mut vec: Vec<char> = Vec::new();
        for c in line.chars() {
            vec.push(c);
        }
        println!("Line: {:?}", vec);
        // println!("{:?}", vec)
        // let direction = vec[0];
        // let distance: i32 = vec[1].parse().unwrap();
    }
    return 0;
}

// pub fn puzzle_b() {
//     println!("\n-- Puzzle B --");
//     // ------------------------------------------------------------------------

//     let contents = fs::read_to_string("day_03/input.txt").unwrap();
//     let position = find_position_b(&contents);
//     let result = position.horizontal * position.depth;

//     println!("Result:\n{:?}", result);

//     // ------------------------------------------------------------------------
// }

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn puzzle_a() {
        let contents = fs::read_to_string("test_input.txt").unwrap();
        let result = find_rates(&contents);
        assert_eq!(result, 1);
    }
    // #[test]
    // fn puzzle_b() {
    //     let contents = fs::read_to_string("day_03/test_input.txt").unwrap();
    //     let result = find_position_b(&contents);
    //     assert_eq!(result.horizontal, 15);
    //     assert_eq!(result.depth, 60);
    // }
}

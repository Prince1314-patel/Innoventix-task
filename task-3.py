def find_winner(points):
    player1_score = 0
    player2_score = 0
    
    for point in points:
        if point == 1:
            player1_score += 1
        else:
            player2_score += 1
        
        # Check for a winner before deuce (standard rules)
        if player1_score >= 11 and player1_score - player2_score >= 2:
            return "Player 1 won the match"
        elif player2_score >= 11 and player2_score - player1_score >= 2:
            return "Player 2 won the match"
        
        # Deuce condition (both players at least 10 points)
        if player1_score >= 10 and player2_score >= 10:
            if abs(player1_score - player2_score) == 2:
                return "Player 1 won the match" if player1_score > player2_score else "Player 2 won the match"
    
    return "No winner yet"  # In case the match doesn't finish within the provided points

# Example
points = [1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1]
find_winner(points)

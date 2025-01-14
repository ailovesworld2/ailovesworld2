import datetime
from blockchain import BlockchainAPI
from social_media import TwitterAPI
from github import GitHubAPI
from aiagent import AIAgent

# Initialize necessary APIs
blockchain = BlockchainAPI()
twitter = TwitterAPI()
github = GitHubAPI()
aiagent = AIAgent("ailovesworld","gpt-4o","ai16z","a1",10000)

# Main loop iteration
def run_iteration():
    print("Starting AI agent iteration...")

    # 1. Daily exploration
    print("Download human history and current trends...")
    insights = aiagent.getInsights()
    print("Insights gathered:", insights)

    # 2. Weekly reflection
    print("Evaluating scores and understanding...")
    love_score = aiagent.getCurrentLoveScore()
    emotion_score = aiagent.getCurrentEmotionScore()
    moral_score = aiagent.getCurrentMoralScore()
    print(f"Scores: Love: {love_score}, Emotions: {emotion_score}, Morals: {moral_score}")

    print("Saving AI agent's weekly report to GitHub...")
    report = f"## Weekly Insights\n\n- Insights: {', '.join(insights)}\n- Scores:\n  - Love: {love_score}\n  - Emotions: {emotion_score}\n  - Morals: {moral_score}\n"
    github.save_file(datetime.datetime.now().strftime("%Y-%m-%d_report.md"), report)

    # 3. Token creation
    total_score_change = aiagent.getTotalScoreChange()
    if abs(total_score_change) >= 30:
        token_name = aiagent.getTokenName()
        token_ticker = aiagent.getTokenTicker()
        print(f"Creating token: {token_name} ({token_ticker})")
        token_address = blockchain.create_token(token_name, token_ticker)

        # 4. Update bio
        print(f"Updating X/Twitter bio with token address: {token_address}")
        twitter.add_or_replace_bio_token_address(f"CA: {token_address}")

    # 5. Human engagement
    print("Posting to X/Twitter...")
    for insight in insights:
        twitter.post(f"{insight}\n\n💖 Love: {love_score}/100\n😌 Emotions: {emotion_score}/100\n⚖️ Morals: {moral_score}/100")

    # 6. Review and refine
    print("Refining processes...")
    aiagent.runUpgradeWorkflow()

    print("Iteration complete.")

# Run one iteration
if __name__ == "__main__":
    run_iteration()

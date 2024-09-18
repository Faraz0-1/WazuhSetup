import openai


openai.api_key = 'YOUR_OPENAI_API_KEY'


log_file_path = '/var/ossec/logs/alerts/alerts.log'  


def read_first_n_logs(file_path, n=20):
    logs = []
    try:
        with open(file_path, 'r') as file:
            for _ in range(n):
                line = file.readline()
                if not line:
                    break
                logs.append(line)
    except FileNotFoundError:
        print(f"Log file not found: {file_path}")
    return logs


def analyze_logs_with_chatgpt(log_data):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": f"Please do an analysis on these logs:\n\n{log_data}"}
        ]
    )
    return response['choices'][0]['message']['content']


logs = read_first_n_logs(log_file_path)
log_data = ''.join(logs)  

# Analyze log data
if log_data:
    chatgpt_response = analyze_logs_with_chatgpt(log_data)
    print("ChatGPT Analysis of Wazuh Logs:\n")
    print(chatgpt_response)

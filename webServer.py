from flask import Flask,jsonify,request
import subprocess
from flask_cors import CORS, cross_origin
import os
import git
import shutil

app = Flask(__name__)
cors = CORS(app)


def getSummaryFromLog(logLlama2):
    # sub1 = "n_keep = 0"
    sub1 = "@@"
    sub2 = "llama_print_timings"
    
    # getting index of substrings
    idx1 = logLlama2.index(sub1)
    idx2 = logLlama2.index(sub2)
    
    res = ''
    # getting elements in between
    for idx in range(idx1 + len(sub1) + 1, idx2):
        res = res + logLlama2[idx]
    return res

def getLastCommitData (repo_url): 
    # clona il repo in una cartella temporanea
    repo = git.Repo.clone_from(repo_url, "temp_repo")

    # ultimo e penultimo commit
    current_commit = repo.head.commit
    previous_commit = current_commit.parents[0] if current_commit.parents else None

    # stampa la differenza
    if previous_commit:
        diff_output = repo.git.diff(previous_commit, current_commit)
        repo.close()
        return diff_output
    else:
        repo.close()
        return "No Data"

@app.route('/getSummary', methods=['POST'])
@cross_origin()
def getSummary():
    linkRepo = request.get_json(force=True)['linkRepo']

    # sposta la directory corrente a quella di llama2
    working_directory = "/Users/alessz/Desktop/llama2/llama.cpp"
    os.chdir(working_directory)

    commitData = getLastCommitData(linkRepo)
    promptPerLLama = "tell me what happened in those commits " + commitData


    # to do: capire meglio questo if, forse inutile. la code review deve avvenire anche se è il primo commit ma il nostro script che ci darà???
    if commitData != "No Data": 
        command = ["./main",
                "-m", "./models/7B/ggml-model-q4_0.bin",
                "-t", "8",
                "-n", "512",
                "-p", promptPerLLama]
        # esecuzione del comando
        try:
            logLLama2 = subprocess.check_output(command, stderr=subprocess.STDOUT, universal_newlines=True)
            summary = getSummaryFromLog(logLLama2)
            shutil.rmtree('temp_repo')
            response = {
                "summary" : summary
            }
        except subprocess.CalledProcessError as e:
            print(f"Errore nell'esecuzione del comando: {e.output}")
            response = {
                "summary": "an error as occurred"
            }
        return jsonify(response)
    else:
        print("Nessun commit")


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port='5001')


# https://github.com/alessaless/tempRepository.git
from lib.graphql.wow_schema import schema

if __name__ == '__main__':
    query_string = '''
    { 
        levelAnswers(levelId: 3333) { 
            levelInfo { 
                levelId
                levelLetters
                answers
            }
            stageInfo {
                stageId
                stageCountry
                stageLandmark
            }
        } 
    }
    '''
    result = schema.execute(query_string)
    print(result.data['levelAnswers'])

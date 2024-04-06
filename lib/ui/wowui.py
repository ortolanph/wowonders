import PySimpleGUI as sg

from lib.service.wow_service import WOWService

TEXT_FONT = ('Helvetica', 16)
ITEM_FONT = ('Helvetica', 18)


class WOWGui:
    controller = WOWService()
    stage_data = dict()
    level_data = dict()
    answer_data: [str] = []

    def __init__(self):
        self.stage_data = self.controller.load_stage_data()

        self.layout = [
            [
                sg.Column([
                    [sg.Frame('Stages', layout=[
                        [sg.Text(f'({len(self.stage_data)}) Stages', font=TEXT_FONT, key="-TOTAL-STAGES-LABEL-")],
                        [sg.Listbox(values=list(self.stage_data.keys()), size=(40, 60),
                                    key='-STAGE-',
                                    font=ITEM_FONT, enable_events=True)]], font=TEXT_FONT)]]),

                sg.Column([
                    [sg.Frame('Levels',
                              [
                                  [sg.Text('Click on a Stage', font=TEXT_FONT, key="-TOTAL-LEVELS-LABEL-")],
                                  [sg.Listbox(values=[], size=(120, 20), key='-LEVELS-',
                                              font=ITEM_FONT, enable_events=True)]], font=TEXT_FONT)],
                    [sg.Frame('Answers',
                              [
                                  [sg.Text('Click on a Level', font=TEXT_FONT, key="-TOTAL-ANSWERS-LABEL-")],
                                  [sg.Listbox(values=[], size=(120, 30), font=ITEM_FONT, expand_y=True,
                                              key="-ANSWERS-")]],
                              font=TEXT_FONT)]
                ], element_justification='center')
            ]
        ]
        self.window = sg.Window('My GUI', self.layout, size=(1200, 800), resizable=True)

    def run(self):
        while True:
            event, values = self.window.read()
            if event == sg.WINDOW_CLOSED or event == 'Exit':
                break
            elif event == '-STAGE-':
                selected_stage = values['-STAGE-'][0]
                stage_id = self.stage_data[selected_stage]
                self.level_data = self.controller.load_levels(stage_id)
                self.window['-TOTAL-LEVELS-LABEL-'].update(value=f'({len(self.level_data)}) Levels')
                self.window['-LEVELS-'].update(values=list(self.level_data.keys()))
                self.window['-ANSWERS-'].update(values=[])
            elif event == '-LEVELS-':
                selected_level = values['-LEVELS-'][0]
                level_id = self.level_data[selected_level]
                self.answer_data = self.controller.load_answers(level_id)
                self.window['-TOTAL-ANSWERS-LABEL-'].update(value=f'({len(self.answer_data)}) Answers')
                self.window['-ANSWERS-'].update(values=[answer for answer in self.answer_data])

        self.window.close()

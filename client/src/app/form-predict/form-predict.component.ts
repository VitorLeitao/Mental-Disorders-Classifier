import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-form-predict',
  standalone: true,
  imports: [],
  templateUrl: './form-predict.component.html',
  styleUrl: './form-predict.component.css',
})
export class FormPredictComponent {
  respostaDaAPI: string = '';
  registro: any = {
    Sadness: null,
    Euphoric: null,
    Exhausted: null,
    Sleep_dissorder: null,
    Mood_Swing: null,
    Suicidal_thoughts: null,
    Anorxia: null,
    Authority_Respect: null,
    Try_Explanation: null,
    Aggressive_Response: null,
    Ignore_Move_On: null,
    Nervous_Break_down: null,
    Admit_Mistakes: null,
    Overthinking: null,
    Sexual_Activity: null,
    Concentration: null,
    Optimisim: null,
  };

  setSelectedOption(event: Event, value: string | number) {
    const target = event.target as HTMLSelectElement;
    const option = target.value;
    if (option) {
      this.registro[value] = option;
    }
  }

  handleSubmit() {
    const url = 'http://127.0.0.1:8000/predict';
    const options = {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(this.registro),
    };

    fetch(url, options)
      .then((response) => response.json())
      .then((data) => {
        console.log('Resposta do servidor:', data);
        //alert(data.answer)
        this.respostaDaAPI = data.answer;
      })
      .catch((error) => {
        console.error('Erro ao fazer a solicitação:', error);
      });
  }
}

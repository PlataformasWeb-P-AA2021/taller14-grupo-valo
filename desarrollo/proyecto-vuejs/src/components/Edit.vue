<template>
    <div class="pt-5">
        <form @submit.prevent="create" method="post">
            <div class="form-group">
                <label for="departamento">Nombre del propietario</label>
                <input
                    type="text"
                    class="form-control"
                    id="departamento"
                    v-model="departamento.nombre_propietario"
                    v-validate="'required'"
                    name="departamento"
                    placeholder="Ingrese el nombre del propietario"
                    :class="{'is-invalid': errors.has('departamento.nombre_propietario') && submitted}">
                <div class="invalid-feedback">
                    Por favor ingrese un nombre valido.
                </div>
            </div>

            <div class="form-group">
                <label for="costo">Costo</label>
                <input
                    type="number"
                    class="form-control"
                    id="costo"
                    v-model="departamento.costo"
                    v-validate="'required'"
                    name="costo"
                    placeholder="Ingrese el costo"
                    :class="{'is-invalid': errors.has('departamento.costo') && submitted}">
                <div class="invalid-feedback">
                    Por favor ingrese un costo valido.
                </div>
            </div>

            <div class="form-group">
                <label for="num_cuartos">Número de cuartos</label>
                <input
                    type="number"
                    class="form-control"
                    id="num_cuartos"
                    v-model="departamento.num_cuartos"
                    v-validate="'required'"
                    name="num_cuartos"
                    placeholder="Ingrese el numero de cuartos"
                    :class="{'is-invalid': errors.has('departamento.num_cuartos') && submitted}">
                <div class="invalid-feedback">
                    Por favor ingrese un numero de cuartos valido.
                </div>
            </div>

            <div class="form-group">
                <label for="edificio">edificio</label>
                <select v-model="departamento.edificio">
                            <option v-for="e in edificiosList" :key="e.url" :value="e.url">{{ e.nombre }} {{ e.tipo }}</option>
                        </select>
            </div>

            <button type="submit" class="btn btn-primary">Actualizar</button>
        </form>
    </div>
</template>

<script>

import axios from 'axios';

export default {
    data() {
        return {
            departamento: {
                nombre_propietario: '',
                costo: '',
                num_cuartos: '',
                edificio: '',
            },
            edificiosList: [],
            submitted: false
        }
    },
    mounted() {
        this.getEdificiosList(),
        axios.get('http://127.0.0.1:8090/api/departamentos/' + this.$route.params.id + '/')
            .then( response => {
                this.departamento = response.data
        });
    },
    methods: {
      getEdificiosList() {
            axios
            .get('http://127.0.0.1:8090/api/edificios/')
            .then(response => {
                this.edificiosList = response.data.results
            })
            .catch(error => {
                console.log(error)
            })

        },
        create: function (e) {
            this.$validator.validate().then(result => {
                this.submitted = true;
                if (!result) {
                    return;
                }
                axios.put(`http://127.0.0.1:8090/api/departamentos/${this.departamento.id}/`,
                        this.departamento
                    )
                    .then(response => {
                        this.$router.push('/index');
                    })
            });
        }
    },
}
</script>

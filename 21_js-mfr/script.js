/** @type {[{}]}*/
var data = dat

var obg = document.getElementById('oc')
var pop = document.getElementById('pop')
var lvl = document.getElementById('lvl')
var sub = document.getElementById('sub')
var res = document.getElementById('res')

function occurrencesByGrade(grade) {
    if (grade == undefined) {
        return 0
    }
    const reducer = (count, curr) => {
        var c = curr[`grade${grade}`]
        if (isNaN(Number(c))) {
            return count + 0
        }else{
            return count + Number(c)
        }
    }
    return data.reduce(reducer, 0)
}

/**
 * Find percentage of population that is a given gender
 * @param {Boolean} [female=false] search for female population instead
 * @returns {Object} population data
 */
function genderPop(female) {
    const a = (x, y) => {
        var f = Number(y['female_num'])
        var m = Number(y['male_num'])
        return x + (isNaN(f) ? 0 : f) + (isNaN(m) ? 0 : m)
    }
    var total = data.reduce(a, 0)
    if (female) {
        const f = (x, y) => {
            var a = Number(y['female_num'])
            return x + (isNaN(a) ? 0 : a)
        }
        var fem = data.reduce(f, 0)
        return {"pop":(fem / total) * 100,
                "gender":"female"}
    }else{
        const f = (x, y) => {
            var a = Number(y['male_num'])
            return x + (isNaN(a) ? 0 : a)
        }
        var fem = data.reduce(f, 0)
        return {"pop":(fem / total) * 100,
                "gender":"male"}
    }
}

function levelEducation(grade) {
    if (grade == undefined) {
        return 0
    }
    const level = (x, y) => {
        var a = Number(y[`grade${grade}`])
        return x + (isNaN(a) ? 0 : 1)
    }
    return data.reduce(level, 0)
}

console.log(occurrencesByGrade(2))

console.log(genderPop())

console.log(levelEducation(13))

sub.addEventListener('click', function() {
    res.innerHTML = ''
    res.innerHTML += (obg.value ? `The number of students in grade ${obg.value} is ${occurrencesByGrade(Number(obg.value))}<br>` : '')
    var a = genderPop(pop.checked)
    res.innerHTML += `The percentage of ${a['gender']}s in schools is ${a['pop'].toFixed(3)}%<br>`
    res.innerHTML += (lvl.value ? `The number of schools with the highest level of education as ${lvl.value} is ${levelEducation(Number(lvl.value))}<br>` : '')
})
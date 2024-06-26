from plutter.Code.plot_circle import create_circle


class PrettyPrinter:
    def __init__(self):
        self.indent = 0
        return

    def visite_ast(self, ast):
        return ast.importation.accept(self) + ast.program.accept(self)

    def visite_importation(self, importation):
        out = ''
        for i in importation.imports:
            out += i.accept(self)
        out += '\n'
        return out

    def visite_import(self, importation):
        return 'import ' + importation.ident.accept(self) + '\n'

    def visite_program(self, program):

        out = 'figure ' + program.name.accept(self) + ' {' + \
              '\n'
        self.indent += 1
        out += program.labels.accept(self) + '\n'
        out += program.declarations.accept(self) + '\n' + program.to_draw.accept(self) + '}\n______________________\n'
        self.indent -= 1  # En réalité avec ce langage, il n'y a pas de problème d'indentation

        return out

    def visite_body_draw(self, body_draw):
        out = ''
        for d in body_draw.to_draw:
            out += self.indent * '\t' + d.accept(self) + '\n'
        return out

    def visite_draw(self, draw):
        out = 'draw ' + draw.expr.accept(self)
        return out

    def visite_body_declaration(self, body_declaration):
        out = ''
        for d in body_declaration.declarations:
            out += self.indent * '\t' + d.accept(self) + '\n'
        return out

    def visite_declaration(self, declaration):
        out = declaration.ident.accept(self) + ' = ' + declaration.expr.accept(self)
        return out

    def visite_expression(self, expression):
        return expression.value.accept(self)

    def visite_point(self, point):
        out = '(' + point.x.accept(self) + ', ' + point.y.accept(self) + ')'
        return out

    def visite_circle(self, circle):
        out = '(' + circle.radius.accept(self) + ', ' + circle.center.accept(self) + ')'
        return out

    def visite_droite(self, droite):
        out = '(' + droite.point1.accept(self) + ', ' + droite.point2.accept(self) + ')'
        return out

    def visite_segment(self, segment):
        out = '[\n'
        self.indent += 1
        for i in range(len(segment.point)-1):
            out += self.indent * '\t' + segment.point[i].accept(self) + ',\n'
        out += self.indent * '\t' + segment.point[-1].accept(self) + '\n'
        self.indent -= 1
        out += self.indent * '\t' + ']'
        return out

    def visite_name(self, name):
        return name.name.accept(self)

    def visite_distance(self, distance):
        return distance.value.accept(self)

    def visite_labels(self, labels):
        out = ''
        for label in labels.labels:
            out += label.accept(self)
        return out

    def visite_label(self, label):
        return self.indent * '\t' + label.ident.accept(self) + ' "' + label.name.accept(self) + '"\n'

    @staticmethod
    def visite_lexem(lexem):
        return lexem.value


class DrawVisitor:
    def __init__(self, compilator):
        self.compilator = compilator
        self.drawing = True
        return

    def visite_ast(self, ast):
        ast.program.accept(self)
        return

    def visite_program(self, program):
        program.name.accept(self)
        program.labels.accept(self)
        program.to_draw.accept(self)
        return

    def visite_name(self, name):
        self.compilator.ax.title.set_text(name.name.value)
        return

    def visite_labels(self, labels):
        for label in labels.labels:
            label.accept(self)
        return

    def visite_body_draw(self, body_draw):
        for d in body_draw.to_draw:
            d.accept(self)
        return

    def visite_draw(self, draw):
        draw.expr.value.accept(self)
        return

    def visite_label(self, label):
        if label.ident.kind == 'kw_xlabel':
            self.compilator.ax.set_xlabel(label.name.accept(self))
        else:
            self.compilator.ax.set_ylabel(label.name.accept(self))
        return

    def visite_point(self, point):
        if self.drawing:
            self.compilator.ax.plot(point.x.accept(self), point.y.accept(self), 'ro')
        else:
            return point.x.accept(self), point.y.accept(self)

    def visite_circle(self, circle):
        self.drawing = False
        x, y = circle.center.accept(self)
        self.drawing = True
        cos, sin = create_circle((x, y),
                                 circle.radius.accept(self))


        self.compilator.ax.plot(cos, sin, 'r')
        return

    def visite_droite(self, droite):
        self.drawing = False
        x1, y1 = droite.point1.accept(self)
        x2, y2 = droite.point2.accept(self)
        self.drawing = True
        self.compilator.ax.plot([x1, x2],
                                [y1, y2], 'r')

        return

    def visite_segment(self, segment):
        for i in range(len(segment.point) - 1):
            self.drawing = False
            x1, y1 = segment.point[i].accept(self)
            x2, y2 = segment.point[i+1].accept(self)
            self.drawing = True
            self.compilator.ax.plot([x1, x2],
                                    [y1, y2], 'r')
        return

    def visite_distance(self, distance):
        return distance.value.accept(self)

    def visite_lexem(self, lexem):
        if lexem.kind == 'ident':
            # Cet appel récursif permet de remonter à la valeur numérique de l'identifiant pour le dessiner
            return self.compilator.parseur.value_ident[lexem.value].accept(self)
        elif lexem.kind == 'string':
            return lexem.value
        else:
            return float(lexem.value)
